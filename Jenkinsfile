pipeline {
    agent none

    stages {
        stage('Sonarqube analysis') {
           agent {     docker   'maven:3-alpine'   }

            steps {

                script {
                    scannerHome = tool 'SonarQube Scanner';

                }
                withSonarQubeEnv('sonar') {
                        sh "${scannerHome}/bin/sonar-scanner" 
                }

            }
        }


    }
}