import { useState } from 'react'
import { sortsDatas } from '../Datas'
import { Button, DatePickerComp, Input, Select } from '../Form'
import { BiChevronDown } from 'react-icons/bi'
import { toast } from 'react-hot-toast'
import { useForm } from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import { PatientValidation } from '../Validation'
import { HiArrowNarrowRight } from 'react-icons/hi'

export function PersonalInfo({ titles, nextStep }) {
  const [title, setTitle] = useState(sortsDatas.title[0])
  const [date, setDate] = useState(new Date())
  const [gender, setGender] = useState(sortsDatas.genderFilter[0])
  const [isLoading, setIsLoading] = useState(false)
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(PatientValidation),
  })

  const onSubmit = data => {
    setIsLoading(true)
    const savePatientPromise = new Promise((resolve, reject) => {
      setTimeout(() => {
        const patient = {
          ...data,
          genre: gender.name,
          bornDate: date.toLocaleDateString('es-ES'),
        }
        if (patient) {
          sessionStorage.setItem('patient', JSON.stringify(patient))
          resolve(patient.fullName)
          nextStep()
          setIsLoading(false)
        } else {
          reject('Error al guardar paciente')
        }
      }, 3000)
    })

    toast.promise(savePatientPromise, {
      loading: 'Guardando paciente...',
      success: fullName => `Paciente ${fullName} guardado con éxito`,
      error: err => err,
    })
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="gap-4 flex-colo">
        {/* select  */}
        {titles && (
          <div className="flex flex-col w-full gap-3">
            <p className="text-sm text-black">Title</p>
            <Select
              selectedPerson={title}
              setSelectedPerson={setTitle}
              datas={sortsDatas.title}
            >
              <div className="w-full p-4 text-sm font-light border rounded-lg flex-btn text-textGray border-border focus:border focus:border-subMain">
                {title?.name} <BiChevronDown className="text-xl" />
              </div>
            </Select>
          </div>
        )}
        {/* cedula */}
        <Input
          label="Cedula"
          color={true}
          type="number"
          register={register('idDocument')}
          error={errors.idDocument}
        />
        {/* fullName */}
        <Input
          label="Nombre Completo"
          color={true}
          type="text"
          name="fullName"
          register={register('fullName')}
          error={errors.fullName}
        />
        {/* phone */}
        <Input
          label="Telefono"
          color={true}
          type="number"
          name="phoneNumber"
          register={register('phoneNumber')}
          error={errors.phoneNumber}
        />
        {/* email */}
        <Input
          label="Correo"
          color={true}
          type="text"
          name="email"
          register={register('email')}
          error={errors.email}
        />
        {!titles && (
          <>
            {/* gender */}
            <div className="flex flex-col w-full gap-3">
              <p className="text-sm text-black">Genero</p>
              <Select
                selectedPerson={gender}
                setSelectedPerson={setGender}
                datas={sortsDatas.genderFilter}
              >
                <div className="w-full p-4 text-sm font-light border rounded-lg flex-btn text-textGray border-border focus:border focus:border-subMain">
                  {gender?.name} <BiChevronDown className="text-xl" />
                </div>
              </Select>
            </div>
            {/* date */}
            <DatePickerComp
              label="Fecha De Nacimiento"
              startDate={date}
              onChange={date => setDate(date)}
            />
            {/* address */}
            <Input
              label="Direccion"
              color={true}
              type="text"
              register={register('address')}
              error={errors.address}
            />
          </>
        )}
        {/* submit */}
        <div className="grid w-full grid-cols-1 gap-4 my-5 sm:grid-cols-1">
          <Button
            label={'Continuar'}
            Icon={HiArrowNarrowRight}
            loading={isLoading}
            onSubmit={onSubmit}
          />
        </div>
      </div>
    </form>
  )
}
