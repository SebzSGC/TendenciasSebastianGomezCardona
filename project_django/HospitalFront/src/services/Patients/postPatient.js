import axios from 'axios'

export async function postPatient(patient, contact, medicalInsurance) {
  patient.bornDate = patient.bornDate.toString()
  patient.phoneNumber = patient.phoneNumber.toString()
  contact.phoneNumber = contact.phoneNumber.toString()
  medicalInsurance.policyNumber = medicalInsurance.policyNumber.toString()
  medicalInsurance.policyValidity = medicalInsurance.policyValidity.toString()
  try {
    const patientResponse = await axios.post(
      'http://127.0.0.1:8000/hospital/patients',
      patient
    )
    console.log(patientResponse.data.message)

    const contactResponse = await axios.post(
      `http://127.0.0.1:8000/hospital/patients/${patient.idDocument}/emergencycontact`,
      contact
    )
    console.log(contactResponse.data.message)

    const medicalInsuranceResponse = await axios.post(
      `http://127.0.0.1:8000/hospital/patients/${patient.idDocument}/medicalinsurance`,
      medicalInsurance
    )
    console.log(medicalInsuranceResponse.data.message)

    return 'Paciente creado con éxito'
  } catch (error) {
    console.error('Error creando el paciente:', error)
    throw error.response ? error.response.data : error.message
  }
}
