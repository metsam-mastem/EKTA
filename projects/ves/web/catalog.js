window.VES_CATALOG = {
  cardTypes: [
    {type:'hardware.mcu',label:'Microcontroller',category:'Hardware',description:'Embedded programmable controller',fields:['architecture','clock_mhz','voltage_v','interfaces']},
    {type:'hardware.processor',label:'Processor',category:'Hardware',description:'General-purpose processing unit',fields:['architecture','cores','frequency_mhz','power_w']},
    {type:'hardware.sensor',label:'Sensor',category:'Hardware',description:'Physical measurement component',fields:['measured_quantity','range','accuracy','interface']},
    {type:'hardware.actuator',label:'Actuator',category:'Hardware',description:'Physical output or motion component',fields:['output_type','voltage_v','current_a']},
    {type:'software.application',label:'Application',category:'Software',description:'User-facing or system application',fields:['language','runtime','version']},
    {type:'software.service',label:'Service',category:'Software',description:'Deployable software service',fields:['protocol','endpoint','availability']},
    {type:'software.firmware',label:'Firmware',category:'Software',description:'Software executing on embedded hardware',fields:['target','language','version']},
    {type:'data.database',label:'Database',category:'Data',description:'Structured data persistence component',fields:['engine','schema','storage_gb']},
    {type:'interface.api',label:'API',category:'Interface',description:'Programmatic interface contract',fields:['style','version','auth']},
    {type:'interface.protocol',label:'Protocol',category:'Interface',description:'Communication protocol or bus',fields:['standard','transport','data_rate']},
    {type:'process.workflow',label:'Workflow',category:'Process',description:'Ordered or event-driven process',fields:['trigger','steps','owner']},
    {type:'system.module',label:'System Module',category:'System',description:'Composable subsystem or module',fields:['responsibility','boundary','interfaces']},
    {type:'material.material',label:'Material',category:'Material',description:'Physical material with engineering properties',fields:['composition','density','thermal_properties']},
    {type:'ai.model',label:'AI Model',category:'AI',description:'Machine learning model or inference endpoint',fields:['family','parameters','runtime','license']}
  ],
  decks: [
    {id:'deck.hardware.core',name:'Universal Hardware',description:'Core physical computing elements',types:['hardware.mcu','hardware.processor','hardware.sensor','hardware.actuator']},
    {id:'deck.embedded.systems',name:'Embedded Systems',description:'Embedded product building blocks',types:['hardware.mcu','hardware.sensor','hardware.actuator','software.firmware','interface.protocol']},
    {id:'deck.software.architecture',name:'Software Architecture',description:'Application, service, data and API elements',types:['software.application','software.service','data.database','interface.api']},
    {id:'deck.ai.systems',name:'AI Systems',description:'Model and inference system elements',types:['ai.model','software.service','data.database','interface.api']},
    {id:'deck.materials',name:'Engineering Materials',description:'Materials and physical component references',types:['material.material','hardware.actuator','hardware.sensor']}
  ],
  views:['Mini','Compact','Standard','Technical','Visual','Game','Node','Exploded','Comparison','Document'],
  boards:['Freeform Canvas','Grid Board','Kanban Board','Mind Map','Flow Board','Architecture Board','Circuit Board','Assembly Board','Timeline','Matrix Board','Map Board','Game Board']
};
