import * as yup from 'yup'

export const PatientValidation = yup.object().shape({
  idDocument: yup
    .number()
    .typeError('Cedula debe ser un número')
    .required('Cedula es obligatorio'),
  fullName: yup
    .string()
    .required('Nombre Completo es obligatorio')
    .matches(/^[a-zA-Z\s]+$/, 'Nombre Completo debe contener solo letras'),
  phoneNumber: yup
    .number()
    .typeError('Telefono debe ser un número')
    .required('Telefono es obligatorio'),
  email: yup
    .string()
    .email('Correo debe ser un email válido')
    .required('Correo es obligatorio'),
  address: yup.string().required('Direccion es obligatoria'),
})

export const ContactValidation = yup.object().shape({
  fullName: yup
    .string()
    .required('Nombre Completo es obligatorio')
    .matches(/^[a-zA-Z\s]+$/, 'Nombre Completo debe contener solo letras'),
  phoneNumber: yup
    .number()
    .typeError('Telefono debe ser un número')
    .required('Telefono es obligatorio'),
  relationship: yup.string().required('Parentesco es obligatorio'),
})

export const MedicalValidation = yup.object().shape({
  nameOfInsuranceCompany: yup
    .string()
    .required('Nombre del seguro medico es obligatorio')
    .matches(
      /^[a-zA-Z\s]+$/,
      'Nombre del seguro medico debe contener solo letras'
    ),
  policyNumber: yup.string().required('La poliza es obligatoria'),
})
