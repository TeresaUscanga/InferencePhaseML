SELECT 
t1.Id,
t1.SepalLength,
t1.SepalWidth,
t1.PetalLength,
t1.PetalWidth,
t2.ClassDescription
FROM `ml-inference-phase-automation.MLInferencePhaseAutomation.IrisFlowersDimensions` t1
inner join `ml-inference-phase-automation.MLInferencePhaseAutomation.FlowerClasses` t2
on t1.IdFlowerClass = t2.Id
limit 3; 