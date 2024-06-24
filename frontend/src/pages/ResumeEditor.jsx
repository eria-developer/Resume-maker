import React from "react";
import { Link, Outlet } from "react-router-dom";

const ResumeEditor = () => {
  return (
    <div className="flex">
      <div className="w-1/4 p-4 bg-purple-100 h-svh">
        <div className="flex flex-col space-y-6">
          <Link to="personal-details/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              1. Enter Personal Details
            </button>
          </Link>
          <Link to="educational-background/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              2. Enter Educational Background
            </button>
          </Link>
          <Link to="work-experience/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              3. Enter Work Experience
            </button>
          </Link>
          <Link to="skills/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              4. Enter Your Skills
            </button>
          </Link>
          <Link to="leadership-roles/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              5. Enter Leadership Roles
            </button>
          </Link>
          <Link to="references/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              6. Enter References
            </button>
          </Link>
          <Link to="certifications-earned/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              7. Enter Certifications
            </button>
          </Link>
          <Link to="projects-worked-on/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              8. Enter Projects
            </button>
          </Link>
          <Link to="languages-spoken/">
            <button className="bg-purple-600 text-white py-2 px-4 text-left w-full rounded">
              9. Enter Languages
            </button>
          </Link>
        </div>
      </div>
      <div className="w-3/4 p-4">
        <Outlet />
      </div>
    </div>
  );
};

export default ResumeEditor;
