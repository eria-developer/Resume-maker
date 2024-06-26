import React from "react";
import { NavLink, Link } from "react-router-dom";

const NavBar = () => {
  const linkClass = ({ isActive }) =>
    isActive
      ? "md:p-4 font-semibold px-0 block bg-purple-500 hover:bg-purple-400 rounded-2xl"
      : "md:p-4 font-semibold px-0 block  rounded-2xl hover:bg-purple-400";

  console.log(linkClass);
  return (
    <>
      <header className="lg:px-16 rounded text-white bg-purple-600 flex flex-wrap items-center py-2 px-4 shadow-md">
        <div className="flex-1 flex justify-between items-center">
          <Link href="#" className="text-xl font-bold">
            ResumeWonder
          </Link>
        </div>

        <label htmlFor="menu-toggle" className="pointer-cursor md:hidden block">
          <svg
            className="fill-current text-gray-900"
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            viewBox="0 0 20 20"
          >
            <title>menu</title>
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"></path>
          </svg>
        </label>
        <input className="hidden" type="checkbox" id="menu-toggle" />

        <div
          className="hidden md:flex md:items-center md:w-auto w-full"
          id="menu"
        >
          <nav>
            <ul className="md:flex items-center justify-between text-base text-white  md:pt-0">
              <li className="mr-2">
                <NavLink className={linkClass} to="/">
                  Home
                </NavLink>
              </li>
              <li className="mr-2">
                <NavLink className={linkClass} to="resume-editor">
                  Resume Editor
                </NavLink>
              </li>
              <li>
                <NavLink className={linkClass} to="export-resume">
                  Export
                </NavLink>
              </li>
            </ul>
          </nav>
        </div>
      </header>
    </>
  );
};

export default NavBar;
