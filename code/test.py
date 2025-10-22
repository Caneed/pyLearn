import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 设置中文显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号

class EllipsoidDistanceSolver:
    def __init__(self, x0, a, b, c):
        """
        初始化椭球面距离求解器
        :param x0: 给定的空间点 (x0, y0, z0)
        :param a, b, c: 椭球面参数
        """
        self.x0 = np.array(x0, dtype=np.float64)
        self.a, self.b, self.c = a, b, c
        self.results = {}  # 存储不同算法的结果
        
    def distance_squared(self, x):
        """计算点x到给定点x0的距离平方"""
        return np.sum((x - self.x0) ** 2)
    
    def constraint(self, x):
        """椭球面约束条件: (x/a)^2 + (y/b)^2 + (z/c)^2 - 1 = 0"""
        return (x[0]/self.a)**2 + (x[1]/self.b)** 2 + (x[2]/self.c)**2 - 1
    
    def conjugate_gradient_method(self, initial_guess=None, tol=1e-8, max_iter=1000):
        """
        使用共轭梯度法求解带约束的优化问题
        通过拉格朗日乘数法将约束问题转化为无约束问题
        """
        start_time = time.time()
        
        # 初始猜测点，默认为椭球面上离x0最近的轴端点
        if initial_guess is None:
            initial_guess = np.array([
                self.a if self.x0[0] > 0 else -self.a,
                self.b if self.x0[1] > 0 else -self.b,
                self.c if self.x0[2] > 0 else -self.c
            ])
        
        # 定义拉格朗日函数及其梯度
        def lagrangian(params):
            x, y, z, lambd = params
            return (x-self.x0[0])**2 + (y-self.x0[1])** 2 + (z-self.x0[2])**2 + \
                   lambd * ((x/self.a)**2 + (y/self.b)** 2 + (z/self.c)**2 - 1)
        
        def gradient(params):
            x, y, z, lambd = params
            dx = 2*(x - self.x0[0]) + 2*lambd*x/(self.a**2)
            dy = 2*(y - self.x0[1]) + 2*lambd*y/(self.b**2)
            dz = 2*(z - self.x0[2]) + 2*lambd*z/(self.c**2)
            dlambda = (x/self.a)**2 + (y/self.b)** 2 + (z/self.c)**2 - 1
            return np.array([dx, dy, dz, dlambda])
        
        # 使用scipy的共轭梯度法求解
        result = minimize(
            lambda p: np.linalg.norm(gradient(p)),  # 最小化梯度的模
            np.concatenate([initial_guess, [0.0]]),  # 初始参数包括拉格朗日乘数
            method='CG',
            tol=tol,
            options={'maxiter': max_iter, 'disp': False}
        )
        
        end_time = time.time()
        optimal_point = result.x[:3]
        distance = np.sqrt(self.distance_squared(optimal_point))
        
        # 存储结果
        self.results['conjugate_gradient'] = {
            'optimal_point': optimal_point,
            'distance': distance,
            'iterations': result.nit,
            'time': end_time - start_time,
            'success': result.success
        }
        
        return optimal_point, distance
    
    def pso_algorithm(self, num_particles=30, max_iter=100, w=0.5, c1=1, c2=1):
        """
        粒子群优化算法求解带约束的优化问题
        通过惩罚函数处理约束条件
        """
        start_time = time.time()
        
        # 初始化粒子群
        dim = 3  # 三维空间
        particles = np.random.rand(num_particles, dim)  # [0,1)区间随机值
        
        # 将粒子映射到椭球坐标系
        angles1 = particles[:, 0] * np.pi  # 极角 [0, π]
        angles2 = particles[:, 1] * 2 * np.pi  # 方位角 [0, 2π)
        scales = 0.5 + 0.5 * particles[:, 2]  # 缩放因子 [0.5, 1.0]
        
        # 转换到笛卡尔坐标系
        x = self.a * scales * np.sin(angles1) * np.cos(angles2)
        y = self.b * scales * np.sin(angles1) * np.sin(angles2)
        z = self.c * scales * np.cos(angles1)
        particles = np.column_stack((x, y, z))
        
        # 初始化速度
        velocities = np.random.randn(num_particles, dim) * 0.1
        
        # 初始化最佳位置
        personal_best = particles.copy()
        personal_best_values = np.array([self.distance_squared(p) for p in particles])
        global_best_idx = np.argmin(personal_best_values)
        global_best = personal_best[global_best_idx]
        global_best_value = personal_best_values[global_best_idx]
        
        # PSO主循环
        iteration = 0
        while iteration < max_iter:
            # 更新速度和位置
            r1 = np.random.rand(num_particles, dim)
            r2 = np.random.rand(num_particles, dim)
            
            velocities = w * velocities + \
                         c1 * r1 * (personal_best - particles) + \
                         c2 * r2 * (global_best - particles)
            
            particles += velocities
            
            # 确保粒子在椭球面上（投影法处理约束）
            for i in range(num_particles):
                # 计算当前点到椭球中心的"椭球距离"
                norm = (particles[i,0]/self.a)**2 + (particles[i,1]/self.b)** 2 + (particles[i,2]/self.c)**2
                if norm > 1e-6:  # 避免除以零
                    scale = 1.0 / np.sqrt(norm)
                    particles[i] *= scale
            
            # 计算适应度值（距离平方）
            current_values = np.array([self.distance_squared(p) for p in particles])
            
            # 更新个人最佳和全局最佳
            improved = current_values < personal_best_values
            personal_best[improved] = particles[improved]
            personal_best_values[improved] = current_values[improved]
            
            current_best_idx = np.argmin(current_values)
            if current_values[current_best_idx] < global_best_value:
                global_best = particles[current_best_idx]
                global_best_value = current_values[current_best_idx]
            
            iteration += 1
        
        end_time = time.time()
        distance = np.sqrt(global_best_value)
        
        # 存储结果
        self.results['pso'] = {
            'optimal_point': global_best,
            'distance': distance,
            'iterations': iteration,
            'time': end_time - start_time,
            'success': True
        }
        
        return global_best, distance
    
    def compare_algorithms(self):
        """比较两种算法的结果"""
        if 'conjugate_gradient' not in self.results or 'pso' not in self.results:
            print("请先运行两种算法")
            return
        
        cg = self.results['conjugate_gradient']
        pso = self.results['pso']
        
        print("算法比较结果：")
        print(f"共轭梯度法：")
        print(f"  最优解：{cg['optimal_point']}")
        print(f"  最短距离：{cg['distance']:.8f}")
        print(f"  迭代次数：{cg['iterations']}")
        print(f"  运行时间：{cg['time']:.6f}秒")
        print(f"  是否成功：{cg['success']}")
        
        print(f"\n粒子群优化算法：")
        print(f"  最优解：{pso['optimal_point']}")
        print(f"  最短距离：{pso['distance']:.8f}")
        print(f"  迭代次数：{pso['iterations']}")
        print(f"  运行时间：{pso['time']:.6f}秒")
        print(f"  是否成功：{pso['success']}")
        
        print(f"\n结果差异：")
        print(f"  距离差异：{abs(cg['distance'] - pso['distance']):.8e}")
        print(f"  点坐标差异：{np.linalg.norm(cg['optimal_point'] - pso['optimal_point']):.8e}")
        
        # 可视化比较
        self._plot_comparison()
    
    def _plot_comparison(self):
        """可视化两种算法的结果比较"""
        cg = self.results['conjugate_gradient']
        pso = self.results['pso']
        
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # 1. 距离比较
        axes[0].bar(['共轭梯度法', '粒子群优化'], [cg['distance'], pso['distance']])
        axes[0].set_title('最短距离比较')
        axes[0].set_ylabel('距离')
        for i, v in enumerate([cg['distance'], pso['distance']]):
            axes[0].text(i, v + 0.01, f'{v:.6f}', ha='center')
        
        # 2. 迭代次数比较
        axes[1].bar(['共轭梯度法', '粒子群优化'], [cg['iterations'], pso['iterations']])
        axes[1].set_title('迭代次数比较')
        axes[1].set_ylabel('迭代次数')
        for i, v in enumerate([cg['iterations'], pso['iterations']]):
            axes[1].text(i, v + 1, str(v), ha='center')
        
        # 3. 运行时间比较
        axes[2].bar(['共轭梯度法', '粒子群优化'], [cg['time'], pso['time']])
        axes[2].set_title('运行时间比较 (秒)')
        axes[2].set_ylabel('时间 (秒)')
        for i, v in enumerate([cg['time'], pso['time']]):
            axes[2].text(i, v + 0.001, f'{v:.6f}', ha='center')
        
        plt.tight_layout()
        plt.show()
        
        # 绘制3D空间中的点
        self._plot_3d_points()
    
    def _plot_3d_points(self):
        """绘制3D空间中的原始点和两个算法找到的最近点"""
        cg_point = self.results['conjugate_gradient']['optimal_point']
        pso_point = self.results['pso']['optimal_point']
        
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # 绘制椭球面（网格）
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x_ellipsoid = self.a * np.cos(u) * np.sin(v)
        y_ellipsoid = self.b * np.sin(u) * np.sin(v)
        z_ellipsoid = self.c * np.cos(v)
        ax.plot_wireframe(x_ellipsoid, y_ellipsoid, z_ellipsoid, color="gray", alpha=0.3)
        
        # 绘制点
        ax.scatter(self.x0[0], self.x0[1], self.x0[2], color='red', s=100, label='原始点')
        ax.scatter(cg_point[0], cg_point[1], cg_point[2], color='blue', s=100, label='共轭梯度法结果')
        ax.scatter(pso_point[0], pso_point[1], pso_point[2], color='green', s=100, label='粒子群优化结果')
        
        # 绘制连接线
        ax.plot([self.x0[0], cg_point[0]], [self.x0[1], cg_point[1]], [self.x0[2], cg_point[2]], 'b--')
        ax.plot([self.x0[0], pso_point[0]], [self.x0[1], pso_point[1]], [self.x0[2], pso_point[2]], 'g--')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('空间点到椭球面的最短距离')
        ax.legend()
        plt.show()

# 示例使用
if __name__ == "__main__":
    # 定义参数
    x0 = [3.0, 2.0, 1.0]  # 给定的空间点
    a, b, c = 2.0, 1.5, 1.0  # 椭球面参数
    
    # 创建求解器实例
    solver = EllipsoidDistanceSolver(x0, a, b, c)
    
    # 使用共轭梯度法求解
    cg_point, cg_distance = solver.conjugate_gradient_method()
    
    # 使用粒子群优化算法求解
    pso_point, pso_distance = solver.pso_algorithm()
    
    # 比较两种算法的结果
    solver.compare_algorithms()