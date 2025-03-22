/*
// this just sets up the fetch request 
const DATASTREAM_ID = "g7qgqjt7276pa"; // specific data stream that we want to access
async function getData() {
    const url = `https://api.georobotix.io/ogc/t18/api/systems/${DATASTREAM_ID}/datastreams`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        console.log(json);
    }
    catch(error) {
        console.error(error.message);
    }
}
*/

import fs from 'fs';
import fetch from 'node-fetch';

const WEATHER_ID = "0tsop3f16nvp8";
const BASE_URL = `https://api.georobotix.io/ogc/t18/api/datastreams/${WEATHER_ID}/observations`;

const START_DATE = "2024-03-18T00:00:00Z";
const END_DATE = "2024-03-20T23:59:59Z";

const PAGE_LIMIT = 100; 
const MAX_PAGES = 10; //right now we are grabbing 1000 records from the start and end date set

async function getAllObservations() {
    let allObservations = [];
    let page = 1;

    while (page <= MAX_PAGES) {
        const url = `${BASE_URL}?startTime=${START_DATE}&endTime=${END_DATE}&page=${page}&limit=${PAGE_LIMIT}`;
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }

            const data = await response.json();

            if (!data.items || data.items.length === 0) {
                console.log(`✅ Data collection complete — Total Records: ${allObservations.length}`);
                break;
            }

            const observations = data.items.map(obs => ({
                observationId: obs.id,
                phenomenonTime: obs.phenomenonTime,
                resultTime: obs.resultTime,
                temperature: obs.result?.temperature || 'N/A',
                pressure: obs.result?.pressure || 'N/A',
                windSpeed: obs.result?.windSpeed || 'N/A',
                windDirection: obs.result?.windDirection || 'N/A'
            }));

            allObservations.push(...observations);
            console.log(`📄 Fetched Page ${page}, Records: ${observations.length}`);

            page++; 

        } catch (error) {
            console.error(`❌ Error fetching observations: ${error.message}`);
            break;
        }
    }

    if (allObservations.length > 0) {
        const csvContent = [
            'Observation ID,Phenomenon Time,Result Time,Temperature (°C),Pressure (hPa),Wind Speed (m/s),Wind Direction (°)',
            ...allObservations.map(obs => 
                `${obs.observationId},${obs.phenomenonTime},${obs.resultTime},${obs.temperature},${obs.pressure},${obs.windSpeed},${obs.windDirection}`
            )
        ].join('\n');

        fs.writeFileSync('test_weather_data.csv', csvContent);
        console.log("✅ Data successfully saved as 'test_weather_data.csv'");
    }
}


getAllObservations();