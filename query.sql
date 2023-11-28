--Отримати інформацію про всі смерті разом з деталями:
-- SELECT Deaths.death_no, Deaths.location, Deaths.method,
--        Episodes.season, Episodes.episode,
--        Deaths.killed_name, Killed.house_name AS killed_house,
--        Deaths.killer_name, Killer.house_name AS killer_house
-- FROM Deaths
-- JOIN Episodes ON Deaths.episode_id = Episodes.episode_id
-- LEFT JOIN Characters AS Killed ON Deaths.killed_name = Killed.name
-- LEFT JOIN Characters AS Killer ON Deaths.killer_name = Killer.name;

--Отримати імена всіх персонажів та кількість смертей, які кожен персонаж спричинив:

-- SELECT Characters.name, Characters.house_name,
--        COUNT(Deaths.death_no) AS num_deaths_caused
-- FROM Characters
-- LEFT JOIN Deaths ON Characters.name = Deaths.killer_name
-- GROUP BY Characters.name, Characters.house_name;

--Отримати загальну кількість смертей для кожного епізоду

-- SELECT Episodes.season, Episodes.episode,
--        COUNT(Deaths.death_no) AS num_deaths
-- FROM Episodes
-- LEFT JOIN Deaths ON Episodes.episode_id = Deaths.episode_id
-- GROUP BY Episodes.season, Episodes.episode;
