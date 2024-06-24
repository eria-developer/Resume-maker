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
import WorkExperience from "./pages/WorkExperience";
import LanguagesSpoken from "./pages/LanguagesSpoken";
import Projects from "./pages/Projects";
import Certifications from "./pages/Certifications";
import LeadershipRoles from "./pages/LeadershipRoles";
import Skills from "./pages/Skills";
import References from "./pages/References";

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
          <Route path="work-experience/" element={<WorkExperience />} />
          <Route path="languages-spoken/" element={<LanguagesSpoken />} />
          <Route path="projects-worked-on" element={<Projects />} />
          <Route path="certifications-earned/" element={<Certifications />} />
          <Route path="leadership-roles/" element={<LeadershipRoles />} />
          <Route path="skills/" element={<Skills />} />
          <Route path="references/" element={<References />} />
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
