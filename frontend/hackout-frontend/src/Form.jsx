import './Form.css'
import axios from 'axios';
import React, { useState } from 'react';
function Form(){
  const [formData, setFormData] = useState({
    country: '',
    state: '',
    city: '',
    pincode: '',
    url: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await   
 axios.post('http://127.0.0.1:8000/api/form/', formData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };
  return(
  <>
  <div className='form-container'>
    <h2>Fill the form to learn about the land</h2>
  <form onSubmit={handleSubmit}>
    <label for="country">Country:</label>
    <input type="text" id="country" name="country" placeholder='Enter the country name here' value={formData.country} onChange={handleChange} required/>

    <label for="state">State:</label>
    <input type="text" id="state" name="state" placeholder='Enter the state name here' value={formData.state} onChange={handleChange} required/>

    <label   
 for="city">City:</label>
    <input type="text" id="city" name="city" placeholder='Enter the city name here' value={formData.city} onChange={handleChange}  required />

    <label for="pincode">Pincode:</label>

    <input type="text" id="pincode" name="pincode" placeholder='Enter the pincode here' value={formData.pincode} onChange={handleChange}  required />
    <h3>Or</h3>
    <label for="google-maps">Google Maps URL:</label>
    <input type='text' id='url' name='url' placeholder='Paste the google maps link here' value={formData.url} onChange={handleChange}/>
    <input className='Submitbtn' type="submit" value="Submit"/>
  </form>
  </div>
  </>
  )
}

export default Form
