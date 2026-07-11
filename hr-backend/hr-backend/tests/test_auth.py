"""认证模块单元测试"""

import pytest
from fastapi import HTTPException
from core.auth import AuthHandler, TokenTypeEnum

handler = AuthHandler()


class TestAuthHandler:
    """AuthHandler 单元测试"""

    def test_encode_decode_login_token(self):
        """验证登录 JWT Token 编码解码双向正确"""
        user_id = "test-user-123"
        tokens = handler.encode_login_token(user_id)
        assert "access_token" in tokens
        assert "refresh_token" in tokens

        decoded = handler.decode_access_token(tokens["access_token"])
        assert decoded == user_id

        decoded_refresh = handler.decode_refresh_token(tokens["refresh_token"])
        assert decoded_refresh == user_id

    def test_update_token_only_returns_access_token(self):
        """验证 update token 只返回 access_token"""
        tokens = handler.encode_update_token("test-user-456")
        assert "access_token" in tokens
        assert "refresh_token" not in tokens

    def test_wrong_token_type_returns_403(self):
        """用 refresh_token 冒充 access_token 时返回 403"""
        refresh = handler._encode_token("test-user", type=TokenTypeEnum.REFRESH_TOKEN)
        with pytest.raises(HTTPException) as exc:
            handler.decode_access_token(refresh)
        assert exc.value.status_code == 403

    def test_decode_invalid_access_token_returns_403(self):
        """无效 access_token 返回 403"""
        with pytest.raises(HTTPException) as exc:
            handler.decode_access_token("invalid-token")
        assert exc.value.status_code == 403

    def test_decode_invalid_refresh_token_returns_401(self):
        """无效 refresh_token 返回 401"""
        with pytest.raises(HTTPException) as exc:
            handler.decode_refresh_token("invalid-token")
        assert exc.value.status_code == 401

    def test_singleton_pattern(self):
        """AuthHandler 是单例，多次初始化返回同一实例"""
        another = AuthHandler()
        assert handler is another
