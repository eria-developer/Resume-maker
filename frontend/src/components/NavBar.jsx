import React from "react";

const NavBar = () => {
  return (
    <>
      <header className="lg:px-16 rounded text-white bg-purple-600 flex flex-wrap items-center py-2 px-4 shadow-md">
        <div className="flex-1 flex justify-between items-center">
          <a href="#" className="text-xl font-bold">
            ResumeGenius
          </a>
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
              <li>
                <a
                  className="md:p-4 font-semibold py- px-0 block hover:bg-purple-400 rounded-2xl"
                  href="#"
                >
                  Home
                </a>
              </li>
              <li>
                <a
                  className="md:p-4 font-semibold px-0 block hover:bg-purple-400 rounded-2xl"
                  href="#"
                >
                  Resume Editor
                </a>
              </li>
              <li>
                <a
                  className="md:p-4 font-semibold px-0 block hover:bg-purple-400 rounded-2xl"
                  href="#"
                >
                  Export
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </header>
    </>
  );
};

export default NavBar;
