pipeline {
    agent any

    environment {
        scannerHome = tool 'SonarQube Scanner'
        sonarToken = credentials('sonar-token')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'bitbucket-app-password', url: 'https://bitbucket.org/your-repo/your-project.git'
            }
        }

        stage('Build') {
            steps {
                // Add your build steps here
                echo "Building the project..."
            }
        }

        stage('SonarQube analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=your-project-key -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${sonarToken}"
                }
            }
        }
    }

    post {
        always {
            junit 'target/surefire-reports/*.xml'
        }
    }
}
