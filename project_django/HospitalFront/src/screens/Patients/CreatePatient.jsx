import { useState } from 'react'
import { Link } from 'react-router-dom'
import { IoArrowBackOutline } from 'react-icons/io5'
import Layout from '../../Layout'
import { PersonalInfo } from '../../components/UsedComp/PersonalInfo'
import { EmergencyContact } from '../../components/UsedComp/EmergencyContact'
import { MedicalInsurance } from '../../components/UsedComp/MedicalInsurance'
import SuccessStep from './successStep'

function CreatePatient() {
  const [step, setStep] = useState(1)

  const handleNextStep = () => {
    setStep(step + 1)
  }

  const handlePreviousStep = () => {
    setStep(step - 1)
  }

  const renderStep = () => {
    switch (step) {
      case 1:
        return <PersonalInfo titles={false} nextStep={handleNextStep} />
      case 2:
        return (
          <EmergencyContact
            nextStep={handleNextStep}
            backStep={handlePreviousStep}
          />
        )
      case 3:
        return (
          <MedicalInsurance
            nextStep={handleNextStep}
            backStep={handlePreviousStep}
          />
        )
      default:
        return <SuccessStep />
    }
  }

  return (
    <Layout>
      <div className="flex items-center gap-4">
        <Link
          to="/patients"
          className="px-4 py-3 bg-white border border-dashed rounded-lg border-subMain text-md"
        >
          <IoArrowBackOutline />
        </Link>
        <h1 className="text-xl font-semibold">Ingresar Paciente</h1>
      </div>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white mt-20 rounded-xl border-[1px] border-border p-6"
      >
        {renderStep()}
      </div>
    </Layout>
  )
}

export default CreatePatient
