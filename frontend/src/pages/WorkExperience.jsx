import React from "react";

const WorkExperience = () => {
  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Work Experience</h2>

      <form>
        <div className="mb-4">
          <label className="block text-gray-700">Job Title</label>
          <input
            type="text"
            name="job_title"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Institution</label>
          <input
            type="text"
            name="institution"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Location</label>
          <input
            type="text"
            name="location"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Start Date</label>
          <input
            type="date"
            name="start_date"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">End Date</label>
          <input
            type="date"
            name="end_date"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Description</label>
          <input
            type="text"
            name="description"
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

export default WorkExperience;
