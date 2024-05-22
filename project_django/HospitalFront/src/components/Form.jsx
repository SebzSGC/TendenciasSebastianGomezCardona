import { Listbox, Menu, Switch } from '@headlessui/react'
import { BiLoaderCircle } from 'react-icons/bi'
import DatePicker, { registerLocale } from 'react-datepicker'
import { es } from 'date-fns/locale/es'
import { FaCheck } from 'react-icons/fa'

export function Input({
  label,
  name,
  type,
  color,
  placeholder,
  register,
  error,
}) {
  return (
    <div className="w-full text-sm">
      <label className="text-sm text-black">{label}</label>
      <input
        name={name}
        id={name}
        {...register}
        type={type}
        placeholder={placeholder}
        className={`w-full bg-transparent text-sm mt-3 p-4 border no-spin ${
          color ? 'border-border font-light' : 'border-white text-black'
        } ${
          error ? 'border-red-500' : 'border-border'
        } rounded-lg focus:border focus:border-subMain`}
      />
      {error && <p className="mt-1 text-sm text-red-500">{error.message}</p>}
    </div>
  )
}

// button

export function Button({ label, onClick, onSubmit, loading, Icon, IconLeft }) {
  return (
    <button
      disabled={loading}
      onClick={onClick}
      onSubmit={onSubmit}
      className={`w-full flex-rows gap-4 hover:opacity-80 transitions bg-subMain text-white text-sm font-medium px-2 py-4 rounded`}
    >
      {loading ? (
        <BiLoaderCircle className="text-2xl text-white animate-spin" />
      ) : (
        <>
          {IconLeft && <Icon className="text-xl text-white" />}
          {label}
          {!IconLeft && <Icon className="text-xl text-white" />}
        </>
      )}
    </button>
  )
}

// select

export function MenuSelect({ children, datas, item: data }) {
  return (
    <div className="relative w-full text-sm">
      <Menu>
        <Menu.Button>{children}</Menu.Button>
        <Menu.Items className="absolute left-0 z-50 flex flex-col gap-4 px-6 py-4 bg-white rounded-md shadow-lg ring-1 ring-border focus:outline-none">
          {datas.map((item, index) => (
            <button
              onClick={() => item.onClick(data)}
              key={index}
              className={`flex gap-4 items-center hover:text-subMain`}
            >
              {item.icon && <item.icon className="text-md text-subMain" />}
              {item.title}
            </button>
          ))}
        </Menu.Items>
      </Menu>
    </div>
  )
}

// select 2

export function Select({ children, selectedPerson, setSelectedPerson, datas }) {
  return (
    <div className="relative w-full text-sm ">
      <div className="w-full">
        <Listbox value={selectedPerson} onChange={setSelectedPerson}>
          <Listbox.Button className={'w-full'}>{children}</Listbox.Button>
          <Listbox.Options className="absolute left-0 z-50 flex flex-col w-full gap-4 px-6 py-4 bg-white rounded-md shadow-lg top-10 ring-1 ring-border focus:outline-none">
            {datas.map(person => (
              <Listbox.Option
                className={`cursor-pointer text-xs hover:text-subMain`}
                key={person.id}
                value={person}
                disabled={person.unavailable}
              >
                {person.name}
              </Listbox.Option>
            ))}
          </Listbox.Options>
        </Listbox>
      </div>
    </div>
  )
}

// switch

export function Switchi({ checked, onChange }) {
  return (
    <>
      <Switch
        checked={checked}
        onChange={onChange}
        className={`${checked ? 'bg-subMain' : 'bg-border'}
        relative inline-flex p-[2px] w-12 cursor-pointer rounded-full transition-all duration-200`}
      >
        <span
          aria-hidden="true"
          className={`${checked ? 'translate-x-5' : 'translate-x-0'}
          pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow-lg transition-all duration-200`}
        />
      </Switch>
    </>
  )
}

// textarea

export function Textarea({ label, name, register, placeholder, rows }) {
  return (
    <div className="w-full text-sm">
      <label className={'text-black text-sm'}>{label}</label>
      <textarea
        name={name}
        rows={rows}
        {...register}
        placeholder={placeholder}
        className={`focus:border-subMain w-full bg-transparent text-sm mt-3 p-4 border border-border rounded font-light 
         `}
      />
    </div>
  )
}

// date picker

export function DatePickerComp({ label, startDate, onChange, maxDate }) {
  registerLocale('es', es)
  return (
    <div className="w-full text-sm">
      <label className={'text-black text-sm'}>{label}</label>

      <DatePicker
        locale="es"
        showMonthDropdown
        showYearDropdown
        dropdownMode="select"
        dateFormat="dd/MM/yyyy"
        selected={startDate}
        onChange={onChange}
        maxDate={maxDate ? maxDate : new Date()}
        minDate={new Date('01-01-1900')}
        className="w-full p-4 mt-3 text-sm font-light bg-transparent border rounded-lg border-border focus:border focus:border-subMain"
      />
    </div>
  )
}

// time picker

export function TimePickerComp({ label, startDate, onChange }) {
  registerLocale('es', es)
  return (
    <div className="w-full text-sm">
      <label className={'text-black text-sm'}>{label}</label>
      <DatePicker
        locale="es"
        selected={startDate}
        onChange={onChange}
        showTimeSelect
        showTimeSelectOnly
        timeIntervals={30}
        timeCaption="Time"
        dateFormat="h:mm aa"
        className="w-full p-4 mt-3 text-sm font-light bg-transparent border rounded-lg border-border focus:border focus:border-subMain"
      />
    </div>
  )
}

// checkbox

export function Checkbox({ label, name, onChange, checked }) {
  return (
    <div className="flex flex-row items-center w-full text-sm">
      {/* design checkbox */}
      <label className="relative cursor-pointer flex-colo">
        <input
          type="checkbox"
          name={name}
          checked={checked}
          onChange={onChange}
          className="absolute w-0 h-0 opacity-0"
        />
        <span
          className={` border rounded  w-5 h-5 flex flex-shrink-0 justify-center items-center mr-2 ${
            checked ? 'border-subMain bg-subMain' : 'border-gray-300 bg-white'
          }`}
        >
          <FaCheck
            className={`text-[10px] ${checked ? 'block text-white' : 'hidden'}`}
          />
        </span>
      </label>

      {label && <p className={'text-black text-xs ml-2'}>{label}</p>}
    </div>
  )
}

// from to date picker

export function FromToDate({ label, startDate, onChange, endDate, bg }) {
  registerLocale('es', es)
  return (
    <div className="flex flex-col w-full gap-2 text-sm">
      {label && <label className={'text-black text-sm'}>{label}</label>}
      <DatePicker
        locale="es"
        selectsRange={true}
        startDate={startDate}
        endDate={endDate}
        onChange={onChange}
        className={`w-full ${
          bg ? bg : 'bg-transparent'
        }  text-xs px-4 h-14 border border-border text-main font-normal rounded-lg focus:border focus:border-subMain`}
      />
    </div>
  )
}
