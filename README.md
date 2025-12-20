# SMS Checker Model Service
This repository contains the backend service and model training code of a dummy SMS spam classifier. More information about the SMS checker can be found on [proksch/sms-checker](https://github.com/proksch/sms-checker). 

The repository, organization and the accompanying releases are used to learn about DevOps practices by student group [doda25-team7](https://github.com/doda25-team7). The work was done in the context of the course [DevOps for Distribued Apps (CS4295)](https://studyguide.tudelft.nl/courses/study-guide/educations/14776) at the TU Delft. The groups organization page links to the associated repositories. 

There are two workflows in this repository:
- ```release.yml```: Trigged every push on the main branch. It bumps the patch version, build the ```model-service``` container image and releases it on the Github's artifact repository. 
- ```model_training.yml```: Manually triggered workflow used to train and publish the SMS classifier model. Once training is complete, the workflow creates a new Github Release containing the new model. 