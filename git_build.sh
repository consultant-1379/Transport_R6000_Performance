#!/bin/bash
#dummy comment
if [ "$2" == "" ]; then
    	echo usage: $0 \<Branch\> \<RState\>
    	exit -1
else
	versionProperties=install/version.properties
	theDate=\#$(date +"%c")
	module=$1
	branch=$2
	workspace=$3
fi

function getProductNumber {
        product=`cat $PWD/build.cfg | awk -F " " '{print $3}'`
}

function setRstate {
        revision=`cat $PWD/build.cfg | awk -F " " '{print $4}'`
	
	if git tag | grep $product-$revision; then
        	rstate=`git tag | grep ${product}-${revision} | tail -1 | sed s/.*-// | perl -nle 'sub nxt{$_=shift;$l=length$_;sprintf"%0${l}d",++$_}print $1.nxt($2) if/^(.*?)(\d+$)/';`
        else
		ammendment_level=05
	        rstate=$revision$ammendment_level
	fi
	mv Transport_R6000_Performance/build/feature-release.xml Transport_R6000_Performance/build/feature-release.${rstate}.xml
	echo "Building rstate:$rstate"
}


function Arm104nexusDeploy {
	RepoURL=https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/assure-releases 

	GroupId=com.ericsson.eniq.netanserver.features
	ArtifactId=$module
	zipName=Transport_R6000_Performance
	
	
	echo "****"	
	echo "Deploying the zip /$zipName-24.2.zip as ${ArtifactId}${rstate}.zip to Nexus...."
    mv target/$zipName-24.2.zip target/${ArtifactId}.zip
	echo "****"	

  	mvn deploy:deploy-file \
	        	-Durl=${RepoURL} \
		        -DrepositoryId=assure-releases \
		        -DgroupId=${GroupId} \
		        -Dversion=${rstate} \
		        -DartifactId=${ArtifactId} \
		        -Dfile=target/${ArtifactId}.zip
		      
}

getProductNumber
setRstate

#add maven command here
mvn package

Arm104nexusDeploy

rsp=$?

if [ $rsp == 0 ]; then

  git tag $product-$rstate
  git pull origin master
  git push origin $product-$rstate 

fi

exit $rsp

#added a test demo comment
