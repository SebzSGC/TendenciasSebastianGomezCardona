def validRole(newRole):
    rolOptions = {
    "1": "Administrador",
    "2": "Doctor",
    "3": "Enfermera",
    "4": "Soporte",
    "5": "Recursos Humanos"
    }
    return rolOptions.get(newRole, "Opción inválida")