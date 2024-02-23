class Employee():
    def __init__(self, fullName, idNumber, email, phoneNumber, bornDate, adress, rol, userName, password):
        self.fullName = fullName
        self.idNumber = idNumber
        self.email = email
        self.phoneNumber = phoneNumber
        self.bornDate = bornDate
        self.adress = adress
        self.rol = rol
        self.userName = userName
        self.password = password

    @classmethod
    def createEmployee(cls, typeValidator):
        print("Por favor ingrese los datos del empleado:")
        fullName = input("Nombre completo: ")
        idNumber = input("Número de identificación: ")
        email = input("Correo electrónico: ")
        phoneNumber = input("Número de teléfono: ")
        bornDate = input("Fecha de nacimiento (YYYY-MM-DD): ")
        adress = input("Dirección: ")
        rol = "Opción inválida"
        while rol == "Opción inválida":
            print("Por favor seleccione el rol del empleado:")
            rol = input("1. Administrador\n2. Doctor\n3. Enfermera\n4. Soporte\n5. Recursos Humanos\n")
            rol = typeValidator.validRole(rol)
        userName = input("Nombre de usuario: ")
        password = input("Contraseña: ")
        return cls(fullName, idNumber, email, phoneNumber, bornDate, adress, rol, userName, password)
    
    def updateEmployee(self, attribute, newInfo):
        correctAttributes ={
            "1": "fullName",
            "2": "idNumber",
            "3": "email",
            "4": "phone",
            "5": "bornDate",
            "6": "adress",
            "7": "rol",
            "8": "userName",
            "9": "password"
        }
        if attribute in correctAttributes:
            setattr(self, correctAttributes[attribute], newInfo)
            return print(f"Empleado: {self.fullName} actualizado con éxito")
        else:
            return print("Opción inválida")

