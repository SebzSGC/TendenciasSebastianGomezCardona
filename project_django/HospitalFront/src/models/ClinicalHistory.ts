export default interface ClinicalHistory {
  id: number
  idPatient: number
  idDoctor: number
  consultReason: string
  symptomatology: string
  diagnosis: string
  date: string
}
