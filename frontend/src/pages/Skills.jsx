import React from "react";

const Skills = () => {
  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Skills</h2>

      <form>
        <div className="mb-4">
          <label className="block text-gray-700">Skill Name</label>
          <input
            type="text"
            name="name"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Profieciency Level</label>
          <input
            type="text"
            name="profieciency_level"
            className="w-full px-3 py-2 border rounded"
          />
        </div>

        <button
          type="submit"
          className="bg-purple-600 text-white py-2 px-4 rounded"
        >
          Save
        </button>
      </form>
    </div>
  );
};

export default Skills;
