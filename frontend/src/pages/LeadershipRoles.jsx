import React from "react";

const LeadershipRoles = () => {
  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Leadership Roles</h2>

      <form>
        <div className="mb-4">
          <label className="block text-gray-700">Role</label>
          <input
            type="text"
            name="role"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Organisation</label>
          <input
            type="text"
            name="organisation"
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

export default LeadershipRoles;
