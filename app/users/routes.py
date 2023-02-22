"""Users module."""
from fastapi import APIRouter, Depends

from app.users.controllers import UserController, RoleController, UserHasRoleController
from app.users.controllers.user_auth_controller import JWTBearer
from app.users.schemas import RoleSchemaIn, RoleSchema, UserSchema, UserSchemaIn, UserHasRoleSchema, \
    UserHasRoleSchemaIn, UserWithRolesSchema, UserSchemaUpdateIsActive

admin_router = APIRouter(tags=["Admin - run once to add initial admin and roles"], prefix="/api/admin")
user_router = APIRouter(tags=["Users"], prefix="/api/users")
role_router = APIRouter(tags=["Roles"], prefix="/api/roles")
user_has_role_router = APIRouter(tags=["User has roles"], prefix="/api/user-has-roles")


@admin_router.post("/setup-admin", response_model=UserSchema)
def setup_admin(user: UserSchemaIn):
    """setup_admin route"""
    admin = UserController.create_user(user.email, user.password)
    admin_role = RoleController.create_role(role_type="ADMIN")
    RoleController.create_role(role_type="USER")
    RoleController.create_role(role_type="PRO_USER")
    UserHasRoleController.create_user_has_role(user_id=admin.user_id, role_id=admin_role.role_id)
    return admin


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    """login_user route"""
    return UserController.login_user(user.email, user.password)


@user_router.post("/add-new-user", response_model=UserSchema,
                  dependencies=[Depends(JWTBearer("ADMIN"))])
def create_user(user: UserSchemaIn):
    """create_user route"""
    user = UserController.create_user(user.email, user.password)
    UserHasRoleController.create_user_has_role(user_id=user.user_id,
                                               role_id=RoleController.read_role_by_type("USER").role_id)
    return user


@user_router.get("/id", response_model=UserSchema,
                 dependencies=[Depends(JWTBearer("USER"))])
def get_user_by_id(user_id: str):
    """get_user_by_id route"""
    return UserController.read_user_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema],
                 dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_users():
    """get_all_users route"""
    return UserController.read_all_users()


@user_router.get("/get-all-users-with-roles", response_model=list[UserWithRolesSchema],
                 dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_users_with_roles():
    """get_all_users_with_roles route"""
    return UserController.read_all_users()


@user_router.get("/get-all-active-users", response_model=list[UserSchema],
                 dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_active_users():
    """get_all_active_users route"""
    return UserController.read_all_active_users()


@user_router.get("/get-all-admins", response_model=list[UserSchema],
                 dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_admins():
    """get_all_admins route"""
    return UserController.read_all_admins()


@user_router.put("/update/is_active", response_model=UserSchema,
                 dependencies=[Depends(JWTBearer("ADMIN"))])
def update_user_is_active(user: UserSchemaUpdateIsActive):
    """update_user_is_active route"""
    return UserController.update_user_is_active(user.user_id, user.is_active)


@user_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_user_by_id(user_id: str):
    """delete_user_by_id route"""
    return UserController.delete_user_by_id(user_id)


@role_router.post("/add-new-role", response_model=RoleSchema,
                  dependencies=[Depends(JWTBearer("ADMIN"))])
def create_role(role: RoleSchemaIn):
    """create_role route"""
    return RoleController.create_role(role.role_type)


@role_router.get("/id", response_model=RoleSchema,
                 dependencies=[Depends(JWTBearer("ADMIN"))])
def get_role_by_id(role_id: str):
    """get_role_by_id route"""
    return RoleController.read_role_by_id(role_id)


@role_router.get("/get-role-by-type", response_model=RoleSchema,
                 dependencies=[Depends(JWTBearer("ADMIN"))])
def get_role_by_type(role_type: str):
    """get_role_by_type route"""
    return RoleController.read_role_by_type(role_type)


@role_router.get("/get-all-roles", response_model=list[RoleSchema],
                 dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_roles():
    """get_all_roles route"""
    return RoleController.read_all_roles()


@role_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_role_by_id(role_id: str):
    """delete_role_by_id route"""
    return RoleController.delete_role_by_id(role_id)


@user_has_role_router.post("/add-new-role-to-user", response_model=UserHasRoleSchema,
                           dependencies=[Depends(JWTBearer("ADMIN"))])
def create_user_has_role(user_has_role: UserHasRoleSchemaIn):
    """create_user_has_role route"""
    return UserHasRoleController.create_user_has_role(user_id=user_has_role.user_id, role_id=user_has_role.role_id)


@user_has_role_router.get("/id", response_model=UserHasRoleSchema,
                          dependencies=[Depends(JWTBearer("ADMIN"))])
def get_user_has_role_by_id(user_has_role_id: str):
    """get_user_has_role_by_id route"""
    return UserHasRoleController.read_user_has_role_by_id(user_has_role_id)


@user_has_role_router.get("/user-id", response_model=list[UserHasRoleSchema],
                          dependencies=[Depends(JWTBearer("ADMIN"))])
def get_user_has_roles_by_user_id(user_id: str):
    """get_user_has_roles_by_user_id route"""
    return UserHasRoleController.read_user_has_roles_by_user_id(user_id)


@user_has_role_router.get("/users-have-roles", response_model=list[UserHasRoleSchema],
                          dependencies=[Depends(JWTBearer("ADMIN"))])
def get_all_users_have_roles():
    """get_all_users_have_roles route"""
    return UserHasRoleController.read_all_users_have_roles()


@user_has_role_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_user_has_role_by_id(user_has_role_id: str):
    """delete_user_has_role_by_id route"""
    return UserHasRoleController.delete_user_has_role_by_id(user_has_role_id)
