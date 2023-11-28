# AWS CLI Usage

## Install

- https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-install.html

```sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

## Configure

- https://zenn.dev/akkie1030/articles/aws-cli-setup-tutorial

```sh
aws configure
```

## Copy

```
aws s3 cp FILE s3://TO/ # --storage-class DEEP_ARCHIVE
```
