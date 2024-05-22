import './App.css'
import { Suspense, lazy } from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Aos from 'aos'
import Toast from './components/Notifications/Toast'
import BigLoader from './components/Notifications/BigLoader'
import Chats from './screens/Chats/Chats'
const Dashboard = lazy(() => import('./screens/Dashboard'))
const Payments = lazy(() => import('./screens/Payments/Payments'))
const Appointments = lazy(() => import('./screens/Appointments'))
const Patients = lazy(() => import('./screens/Patients/Patients'))
const Campaings = lazy(() => import('./screens/Campaings'))
const Services = lazy(() => import('./screens/Services'))
const Invoices = lazy(() => import('./screens/Invoices/Invoices'))
const Settings = lazy(() => import('./screens/Settings'))
const CreateInvoice = lazy(() => import('./screens/Invoices/CreateInvoice'))
const EditInvoice = lazy(() => import('./screens/Invoices/EditInvoice'))
const PreviewInvoice = lazy(() => import('./screens/Invoices/PreviewInvoice'))
const EditPayment = lazy(() => import('./screens/Payments/EditPayment'))
const PreviewPayment = lazy(() => import('./screens/Payments/PreviewPayment'))
const Medicine = lazy(() => import('./screens/Medicine'))
const PatientProfile = lazy(() => import('./screens/Patients/PatientProfile'))
const CreatePatient = lazy(() => import('./screens/Patients/CreatePatient'))
const Doctors = lazy(() => import('./screens/Doctors/Doctors'))
const DoctorProfile = lazy(() => import('./screens/Doctors/DoctorProfile'))
const Receptions = lazy(() => import('./screens/Receptions'))
const NewMedicalRecode = lazy(() =>
  import('./screens/Patients/NewMedicalRecode')
)
const NotFound = lazy(() => import('./screens/NotFound'))
const Login = lazy(() => import('./screens/Login'))
const Reviews = lazy(() => import('./screens/Reviews'))

function App() {
  Aos.init()

  return (
    <>
      {/* Toaster */}
      <Toast />
      {/* Routes */}
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <Suspense fallback={<BigLoader />}>
                <Dashboard />
              </Suspense>
            }
          />
          {/* invoce */}
          <Route
            path="/invoices"
            element={
              <Suspense fallback={<BigLoader />}>
                <Invoices />
              </Suspense>
            }
          />
          <Route
            path="/invoices/create"
            element={
              <Suspense fallback={<BigLoader />}>
                <CreateInvoice />
              </Suspense>
            }
          />
          <Route
            path="/invoices/edit/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <EditInvoice />
              </Suspense>
            }
          />
          <Route
            path="/invoices/preview/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <PreviewInvoice />
              </Suspense>
            }
          />
          {/* payments */}
          <Route
            path="/payments"
            element={
              <Suspense fallback={<BigLoader />}>
                <Payments />
              </Suspense>
            }
          />
          <Route
            path="/payments/edit/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <EditPayment />
              </Suspense>
            }
          />
          <Route
            path="/payments/preview/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <PreviewPayment />
              </Suspense>
            }
          />
          {/* patient */}
          <Route
            path="/patients"
            element={
              <Suspense fallback={<BigLoader />}>
                <Patients />
              </Suspense>
            }
          />
          <Route
            path="/patients/preview/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <PatientProfile />
              </Suspense>
            }
          />
          <Route
            path="/patients/create"
            element={
              <Suspense fallback={<BigLoader />}>
                <CreatePatient />
              </Suspense>
            }
          />
          <Route
            path="/patients/visiting/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <NewMedicalRecode />
              </Suspense>
            }
          />
          {/* doctors */}
          <Route
            path="/doctors"
            element={
              <Suspense fallback={<BigLoader />}>
                <Doctors />
              </Suspense>
            }
          />
          <Route
            path="/doctors/preview/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <DoctorProfile />
              </Suspense>
            }
          />
          {/* reception */}
          <Route
            path="/receptions"
            element={
              <Suspense fallback={<BigLoader />}>
                <Receptions />
              </Suspense>
            }
          />
          {/* others */}
          <Route
            path="/login"
            element={
              <Suspense fallback={<BigLoader />}>
                <Login />
              </Suspense>
            }
          />
          <Route
            path="/appointments"
            element={
              <Suspense fallback={<BigLoader />}>
                <Appointments />
              </Suspense>
            }
          />
          <Route
            path="/campaigns"
            element={
              <Suspense fallback={<BigLoader />}>
                <Campaings />
              </Suspense>
            }
          />
          <Route
            path="/medicine"
            element={
              <Suspense fallback={<BigLoader />}>
                <Medicine />
              </Suspense>
            }
          />
          <Route
            path="/services"
            element={
              <Suspense fallback={<BigLoader />}>
                <Services />
              </Suspense>
            }
          />
          <Route
            path="/settings"
            element={
              <Suspense fallback={<BigLoader />}>
                <Settings />
              </Suspense>
            }
          />
          {/* reviews */}
          <Route
            path="/reviews"
            element={
              <Suspense fallback={<BigLoader />}>
                <Reviews />
              </Suspense>
            }
          />
          {/* chats */}
          <Route
            path="/chats"
            element={
              <Suspense fallback={<BigLoader />}>
                <Chats />
              </Suspense>
            }
          />
          <Route
            path="*"
            element={
              <Suspense fallback={<BigLoader />}>
                <NotFound />
              </Suspense>
            }
          />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
