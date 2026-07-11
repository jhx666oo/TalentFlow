"""pytest 全局配置"""

import pytest


pytest_plugins = []


def pytest_configure(config):
    """注册自定义标记"""
    config.addinivalue_line("markers", "integration: 集成测试，依赖数据库/Redis")
    config.addinivalue_line("markers", "slow: 需要较长时间的测试")
