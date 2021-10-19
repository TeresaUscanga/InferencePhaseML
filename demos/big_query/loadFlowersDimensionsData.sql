begin 
    
    begin transaction; 

    insert into `ml-inference-phase-automation.MLInferencePhaseAutomation.IrisFlowersDimensions` 
    (Id, SepalLength, SepalWidth, PetalLength, PetalWidth, IdFlowerClass, CreationDate, UpdateDate, Comment)
    SELECT 
    GENERATE_UUID() as Id,
    cast(t1.sepal_length as NUMERIC) as SepalLength, 
    cast(t1.sepal_width as NUMERIC) as SepalWidth,
    cast(t1.petal_length as NUMERIC) as PetalLength,
    cast(t1.petal_width as NUMERIC) as PetalWidth,
    t2.Id as IdFlowerClass,
    CURRENT_DATETIME() as CreationDate,
    CURRENT_DATETIME() as UpdateDate,
    "Added" as Comment
    FROM `ml-inference-phase-automation.MLInferencePhaseAutomation.ChargeIrisFlowerDataCSV` t1
    inner join `ml-inference-phase-automation.MLInferencePhaseAutomation.FlowerClasses` t2
    on t1.class = t2.ClassDescription;
    
    select * from `ml-inference-phase-automation.MLInferencePhaseAutomation.IrisFlowersDimensions`;

    rollback transaction;

    select * from `ml-inference-phase-automation.MLInferencePhaseAutomation.IrisFlowersDimensions`;

    -- commit transaction; 
end