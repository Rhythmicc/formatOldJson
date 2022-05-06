# formatOldJson



帮助你快速将[Qpro](https://github.com/Rhythmicc/QuickProject)的旧配置表更换为最新版本的格式。

1. 克隆此项目。
2. `Qpro register-global` [将本仓库注册为全局命令](https://rhythmlian.cn/2020/02/14/QuickProject/#%E5%B0%86Commander%E5%BA%94%E7%94%A8%E6%B3%A8%E5%86%8C%E4%B8%BA%E5%85%A8%E5%B1%80%E5%91%BD%E4%BB%A4)。
3. 安装[`fd`命令](https://github.com/sharkdp/fd)
4. 替换: `formatOldJson allFormat -filepath $(fd project_configure.json)`
