import React from "react";

import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import HomePage from "./pages/HomePage";
import ResumeEditor from "./pages/ResumeEditor";
import ExportResume from "./pages/ExportResume";
import NotFound from "./pages/NotFound";
import PersonalDetails from "./pages/PersonalDetails";
import EducationalBackground from "./pages/EducationalBackground";

function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<MainLayout />}>
        <Route index element={<HomePage />} />
        <Route path="resume-editor/" element={<ResumeEditor />}>
          <Route path="personal-details/" element={<PersonalDetails />} />
          <Route
            path="educational-background/"
            element={<EducationalBackground />}
          />
          <Route path="personal-details/" element={<PersonalDetails />} />
          <Route path="personal-details/" element={<PersonalDetails />} />
          <Route path="personal-details/" element={<PersonalDetails />} />
          <Route path="personal-details/" element={<PersonalDetails />} />
          <Route path="personal-details/" element={<PersonalDetails />} />
          <Route path="personal-details/" element={<PersonalDetails />} />
          <Route path="personal-details/" element={<PersonalDetails />} />
        </Route>
        <Route path="export-resume/" element={<ExportResume />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    )
  );

  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
