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


// grabbing PDF data from : https://www.weather.gov/wrh/Climate?wfo=hun

// grabbing weather conditions from : https://www.ncdc.noaa.gov/stormevents/listevents.jsp?eventType=ALL&beginDate_mm=01&beginDate_dd=01&beginDate_yyyy=2023&endDate_mm=12&endDate_dd=31&endDate_yyyy=2024&county=MADISON%3A89&hailfilter=0.00&tornfilter=0&windfilter=000&sort=DT&submitbutton=Search&statefips=1%2CALABAMA
import fs from 'fs';
import fetch from 'node-fetch';

const WEATHER_ID = "0tsop3f16nvp8";
const HURRICANE_ID = "4knoao0uki8bq";

const START_DATE = "2023-01-01T00:00:00Z";
const END_DATE = "2024-12-31T23:59:59Z";
// we want to grab data every 60 minutes instead of every minute 

const PAGE_LIMIT = 100; 
const MAX_PAGES = 10; //right now we are grabbing 1000 records from the start and end date set

async function getAllObservations() {
    let allObservations = [];
    let page = 1;

    const BASE_URL = `https://api.georobotix.io/ogc/t18/api/datastreams/${WEATHER_ID}/observations`;
    while (page <= MAX_PAGES) {
        const url = `${BASE_URL}?startTime=${START_DATE}&endTime=${END_DATE}&page=${page}&limit=${PAGE_LIMIT}`;
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }

            const data = await response.json();

            if (!data.items || data.items.length === 0) {
                console.log(`Data collection complete — Total Records: ${allObservations.length}`);
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
            console.log(`Fetched Page ${page}, Records: ${observations.length}`);

            page++; 

        } catch (error) {
            console.error(`Error fetching observations: ${error.message}`);
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
        console.log("Data successfully saved as 'test_weather_data.csv'");
    }
}


//getAllObservations();

async function getHurricaneData() {
    let allObservations = [];
    let page = 1;
    const BASE_URL = `https://api.georobotix.io/ogc/t18/api/datastreams/${HURRICANE_ID}/observations`;

    while (page <= MAX_PAGES) {
        const url = `${BASE_URL}?startTime=${START_DATE}&endTime=${END_DATE}&page=${page}&limit=${PAGE_LIMIT}`;
        
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }

            const data = await response.json();

            if (!data.items || data.items.length === 0) {
                console.log(`Hurricane data collection complete — Total Records: ${allObservations.length}`);
                break;
            }

            // grab one observation and see what it looks like
          //  console.log(data.items[0]);


            const observations = data.items.map(obs => ({
                observationId: obs.id,
                phenomenonTime: obs.phenomenonTime,
                resultTime: obs.resultTime,
                location: obs.result?.location 
                    ? `${obs.result.location.lat} + ${obs.result.location.lon}` 
                    : 'N/A',
                airTemperature: obs.result?.TEMP_AIR_MEAN,
                relativeHumidity: obs.result?.RH_MEAN,
                airPressure: obs.result?.BARO_PRES_MEAN ,
                seawaterTemperature: obs.result?.TEMP_SBE37_MEAN ,
                windDirection: obs.result?.WIND_FROM_MEAN ,
                windSpeed: obs.result?.WIND_SPEED_MEAN ,
                seawaterSalinity: obs.result?.SAL_SBE37_MEAN ,
                waterCurrentSpeed: obs.result?.WATER_CURRENT_SPEED_MEAN ,
                waterCurrentDirection: obs.result?.WATER_CURRENT_DIRECTION_MEAN,
                dominantWavePeriod: obs.result?.WAVE_DOMINANT_PERIOD ,
                significantWaveHeight: obs.result?.WAVE_SIGNIFICANT_HEIGHT 
            }));

            allObservations.push(...observations);
            console.log(`Fetched Page ${page}, Records: ${observations.length}`);

            page++;

        } catch (error) {
            console.error(`Error fetching hurricane data: ${error.message}`);
            break;
        }
    }

    if (allObservations.length > 0) {
        const csvContent = [
            'Observation ID,Phenomenon Time,Result Time,Location,Air Temperature (°C),Relative Humidity (%),Air Pressure (hPa),Seawater Temperature (°C),Wind Direction (°),Wind Speed (m/s),Seawater Salinity (PSU),Water Current Speed (m/s),Water Current Direction (°),Dominant Wave Period (s),Significant Wave Height (m)',
            ...allObservations.map(obs => 
                `${obs.observationId},${obs.phenomenonTime},${obs.resultTime},${obs.location},${obs.airTemperature},${obs.relativeHumidity},${obs.airPressure},${obs.seawaterTemperature},${obs.windDirection},${obs.windSpeed},${obs.seawaterSalinity},${obs.waterCurrentSpeed},${obs.waterCurrentDirection},${obs.dominantWavePeriod},${obs.significantWaveHeight}`
            )
        ].join('\n');

        fs.writeFileSync('hurricane_data.csv', csvContent);
        console.log("Hurricane data successfully saved as 'hurricane_data.csv'");
    }
}

//getHurricaneData();


