from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    오직 소유자만 해당 객체 수정 가능
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모든 요청에 허용 (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 오직 소유자에게만 부여
        return obj == request.user
