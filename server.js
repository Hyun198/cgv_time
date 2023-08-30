const getTime = require('./getTime');
const crawling = require('./crawling');
require('dotenv').config();
const express = require('express');
const puppeteer = require('puppeteer');
const schedule = require('node-schedule');
const fs = require('fs/promises')
const path = require('path')
const app = express();

app.set('view engine', 'ejs');
app.use(express.static('public'));


async function InitialCrawling() {
    try {
        const browser = await puppeteer.launch({ headless: true });
        const page = await browser.newPage();
        await page.goto(process.env.cgv);
        const times = await page.evaluate(() =>{
            return Array.from(document.querySelectorAll(".movie_content._wrap_time_table  span.time_info a")).map(x => x.textContent)
        });

        await browser.close();

        const data = { times };

        
        console.log('Initial crawling completed');
    } catch (err) {
        console.error('error during initial crawling:', err);
    }
}
InitialCrawling();



app.get('/', async (req, res) => {
    const hourlyCrawling = schedule.scheduleJob('*/5 * * * *', () => {
        console.log('performing hourly crawling...');
        crawling.performCrawling();
    });
    try{
        const cachedFilePath = path.join('cgv', 'cached_Data.txt');
        //파일 캐싱 : 데이터 저장
        let cachedData = await fs.readFile(cachedFilePath, 'utf-8').catch(() => null);
        //캐시 데이터가 없으면 초기 크롤링 수행
        if(!cachedData) {
            console.log('Cached data not found. performing inital crawling...');
            await crawling.performCrawling();
            cachedData = await fs.readFile(cachedFilePath, 'utf-8');
        }
            //파일캐싱 : 데이터 사용
            //const parsedData = JSON.parse(cachedData);

            const times = cachedData.split("\n").filter(line => line.trim() !== '');
            
            
            const timesFilePath = path.join('cgv', 'cached_Data.txt');
            const {minTime, maxTime} = await getTime.calculateTime(timesFilePath); 
        
        res.render('cgv',{minTime, maxTime, times});
    }catch(err){
        console.error(err);
        res.status(500).send('에러발생');
    }
});

app.listen(PORT=8000, () => {
    console.log(`server is running on ${PORT}`)
})




/* const MorningCrawling = schedule.scheduleJob('0 7 * * *', async () => {
    try {
        
        const morningFilePath = path.join('cgv', 'morning_data.txt');
        let morningData = await fs.readFile(morningFilePath, 'utf-8').catch(() => null);
        

        if(!morningData) {
            console.log('Morning_Cached data not found. performing inital crawling...');
            await crawling.morningCrawling();
            morningData = await fs.readFile(morningFilePath, 'utf-8');
        }

        const times = morningData.split("\n").filter(line => line.trim() !== '');

        const timesFilePath = path.join('cgv', 'morning_data.txt');

        const {minTime, maxTime} = await getTime.calculateTime(timesFilePath); 
        console.log('Crawling at 7am completed');

    } catch (error) {
        console.error('Error: ', error);
    }
}); */