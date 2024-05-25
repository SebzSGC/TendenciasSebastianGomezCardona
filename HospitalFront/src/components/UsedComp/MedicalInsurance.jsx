import { HiArrowNarrowLeft, HiArrowNarrowRight } from 'react-icons/hi'
import { Button, DatePickerComp, Input, Switchi } from '../Form'
import { useForm } from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import { MedicalValidation } from '../Validation'
import toast from 'react-hot-toast'
import { useState } from 'react'
import { postPatient } from '../../services/Patients/postPatient'

export function MedicalInsurance({ nextStep, backStep, button = true }) {
  const [date, setDate] = useState(new Date())
  const [isLoading, setIsLoading] = useState(false)
  const [check, setCheck] = useState(false)
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(MedicalValidation),
  })

  const onSubmit = data => {
    setIsLoading(true)

    const saveInsurancePromise = new Promise((resolve, reject) => {
      setTimeout(async () => {
        try {
          const patient = JSON.parse(sessionStorage.getItem('patient'))
          const contact = JSON.parse(sessionStorage.getItem('contact'))
          const medicalInsurance = {
            ...data,
            idPatient: patient.idDocument,
            policyValidity: date.toLocaleDateString('es-ES'),
            policyState: check ? true : false,
          }

          if (medicalInsurance && patient && contact) {
            const response = await postPatient(
              patient,
              contact,
              medicalInsurance
            )
            resolve(response)

            sessionStorage.removeItem('patient')
            sessionStorage.removeItem('contact')
            nextStep()
          } else {
            sessionStorage.removeItem('patient')
            sessionStorage.removeItem('contact')
            reject('Error al guardar el paciente en la base de datos')
          }
        } catch (error) {
          reject(error)
        } finally {
          setIsLoading(false)
        }
      }, 3000)
    })

    toast.promise(saveInsurancePromise, {
      loading: 'Guardando paciente en la base de datos...',
      success: 'Paciente creado con éxito',
      error: 'Error al guardar el paciente en la base de datos',
    })
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="gap-4 flex-colo">
        <div className="flex flex-col w-full gap-3">
          <p className="my-5 text-base text-center text-black">Seguro medico</p>
          <div className="grid w-full gap-3 sm:grid-cols-2">
            <Input
              label="Nombre"
              color={true}
              type="text"
              register={register('nameOfInsuranceCompany')}
              error={errors.nameOfInsuranceCompany}
            />
            <Input
              label="Numero de poliza"
              color={true}
              type="number"
              register={register('policyNumber')}
              error={errors.policyNumber}
            />
            <div className="py-1 text-sm text-black">
              Estado de poliza
              <div className="flex items-center w-full gap-2 py-5 ">
                <Switchi checked={check} onChange={() => setCheck(!check)} />
                <p
                  className={`text-sm ${
                    check ? 'text-subMain' : 'text-textGray'
                  }`}
                >
                  {check ? 'Activo' : 'Inactivo'}
                </p>
              </div>
            </div>
            <DatePickerComp
              label="Fecha De Vencimiento"
              startDate={date}
              onChange={date => setDate(date)}
              maxDate={new Date('2050-12-31')}
            />
          </div>
        </div>
        {/* submit */}
        {button && (
          <div className="grid w-full grid-cols-1 gap-4 my-5 sm:grid-cols-2">
            <Button
              label={'Regresar'}
              Icon={HiArrowNarrowLeft}
              IconLeft={true}
              loading={isLoading}
              onClick={() => {
                backStep()
              }}
            />
            <Button
              label={'Confirmar Paciente'}
              Icon={HiArrowNarrowRight}
              loading={isLoading}
              onSubmit={onSubmit}
            />
          </div>
        )}
      </div>
    </form>
  )
}
