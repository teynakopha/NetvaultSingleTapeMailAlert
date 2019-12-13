pipeline{
  environment {
    registry = "harbor.its.local/library/myweb"
    dockerImage = ""
  }

    agent any
    stages{
        stage("Check out git"){
            steps{
                echo "====++++git clone repository++++===="
                git 'https://github.com/teynakopha/jenkins-play.git'
            }
        }
        stage("build image"){
            steps{
                script{
                    dockerImage =  docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage("push image"){
            steps{
                docker.withRegistry( "" ) {
                    dockerImage.push()
                }
            }
        }
        stage("deploy app"){
            steps{
                kubernetesDeploy(configs: "NetvaultCheckCapa.yaml", kubeconfigId: "newkubeconfig")
            }
        }

    }

}