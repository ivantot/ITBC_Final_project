from fastapi import APIRouter, Depends

from app.users.controllers import UserController, RoleController, UserHasRoleController
from app.users.controllers.user_auth_controller import JWTBearer
from app.users.schemas import RoleSchemaIn, RoleSchema, UserSchema, UserSchemaIn, UserHasRoleSchema, UserHasRoleSchemaIn

admin_router = APIRouter(tags=["admin - run once to add initial admin and roles"], prefix="/api/admin")
user_router = APIRouter(tags=["users"], prefix="/api/users")
role_router = APIRouter(tags=["roles"], prefix="/api/roles")
user_has_role_router = APIRouter(tags=["user_has_roles"], prefix="/api/user-has-roles")


@admin_router.post("/setup-admin", response_model=UserSchema)
def setup_admin(user: UserSchemaIn):
    admin = UserController.create_user(user.email, user.password)
    admin_role = RoleController.create_role(role_type="ADMIN")
    RoleController.create_role(role_type="USER")
    RoleController.create_role(role_type="PRO_USER")
    UserHasRoleController.create_user_has_role(user_id=admin.user_id, role_id=admin_role.role_id)
    return admin


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    user = UserController.create_user(user.email, user.password)
    UserHasRoleController.create_user_has_role(user_id=user.user_id,
                                               role_id=RoleController.read_role_by_type("USER").role_id)
    return user


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.read_user_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.read_all_users()


@user_router.get("/get-all-admins", response_model=list[UserSchema])
def get_all_admins():
    return UserController.read_all_admins()


@user_router.put("/update/is_active", response_model=UserSchema)
def update_user(user_id: str, is_active: bool):
    return UserController.update_user_is_active(user_id, is_active)


@user_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


@role_router.post("/add-new-role", response_model=RoleSchema)
def create_role(role: RoleSchemaIn):
    return RoleController.create_role(role.role_type)


@role_router.get("/id", response_model=RoleSchema)
def get_role_by_id(role_id: str):
    return RoleController.read_role_by_id(role_id)


@role_router.get("/get-role-by-type", response_model=RoleSchema)
def get_role_by_type(role_type: str):
    return RoleController.read_role_by_type(role_type)


@role_router.get("/get-all-roles", response_model=list[RoleSchema])
def get_all_roles():
    return RoleController.read_all_roles()


@role_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_role_by_id(role_id: str):
    return RoleController.delete_role_by_id(role_id)


@user_has_role_router.post("/add-new-role-to-user", response_model=UserHasRoleSchema)
def create_user_has_role(user_has_role: UserHasRoleSchemaIn):
    return UserHasRoleController.create_user_has_role(user_id=user_has_role.user_id, role_id=user_has_role.role_id)


@user_has_role_router.get("/id", response_model=UserHasRoleSchema)
def get_user_has_role_by_id(user_has_role_id: str):
    return UserHasRoleController.read_user_has_role_by_id(user_has_role_id)


@user_has_role_router.get("/user-id", response_model=list[UserHasRoleSchema])
def get_user_has_roles_by_user_id(user_id: str):
    return UserHasRoleController.read_user_has_roles_by_user_id(user_id)


@user_has_role_router.delete("/", dependencies=[Depends(JWTBearer("ADMIN"))])
def delete_user_has_role_by_id(user_has_role_id: str):
    return UserHasRoleController.delete_user_has_role_by_id(user_has_role_id)
