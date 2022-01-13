#!/usr/bin/env python3

from boto3.session import Session
import boto3
from decouple import config
from prettytable import PrettyTable
import os
import sys


def get_client():
    """
    Method to return a boto3 Session Client object for S3 service
    """
    return Session().client(
        's3',
        aws_access_key_id=config('S3_ACCESS_KEY'),
        aws_secret_access_key=config('S3_SECRET_ACCESS_KEY'),
    )


def list_buckets():
    """
    Method to print a list of S3 buckets we have access to
    """
    response = get_client().list_buckets()
    if buckets := response.get('Buckets'):
        print(f'Found {len(buckets)} buckets!')
        data = PrettyTable()
        for bucket in buckets:
            data.add_row(bucket.values())
        data.field_names = bucket.keys()
        print(data)
    else:
        print('No buckets found! Create one.')


def create_bucket():
    """
    Method to create an S3 bucket
    """
    bucket_name = input('Enter a name for your S3 bucket : ')
    try:
        get_client().create_bucket(Bucket=bucket_name)
        print(f'S3 bucket with name {bucket_name} has been succesfully created!')
    except Exception as e:
        print(e)


def delete_bucket():
    """
    Method to delete an S3 bucket
    """
    print("Here is a list of your buckets:-")
    list_buckets()
    bucket_name = input('\nEnter the name of the S3 bucket you wish to delete: ')
    try:
        get_client().delete_bucket(
            Bucket=bucket_name,
        )
        print(f'S3 bucket with the name {bucket_name} has been deleted!')
    except Exception as e:
        print(e)


def list_files(bucket_name: str = None):
    """
    Method to list the files in an S3 bucket
    """
    if bucket_name is None:
        print("Here is a list of your buckets:-")
        list_buckets()
        bucket_name = input('\nEnter the name of the S3 bucket you want a list files for: ')
    try:
        response = get_client().list_objects_v2(Bucket=bucket_name)
        if files := response.get('Contents'):
            data = PrettyTable()
            for file in files:
                data.add_row(file.values())
            data.field_names=file.keys()
            print(data)
        else:
            print('No files found in this bucket! Upload one.')
    except Exception as e:
        print(e)


def upload_file():
    """
    Method to upload a file to an S3 bucket
    """
    print("Here is a list of your buckets:-")
    list_buckets()
    bucket_name = input('\nEnter the name of the S3 bucket you to upload a file to: ')
    file_path = input(
        f'Enter the path to the file you wish to upload to {bucket_name}: '
    )
    if not os.path.isfile(file_path):
        print(f'{file_path} does not exist!')
    file_name = os.path.basename(file_path)
    key = (
        input(
            f'Enter the key (filename) you wish to upload {file_path} as (default {file_name}): '
        )
        or file_name
    )
    try:
        get_client().upload_file(
            Bucket=bucket_name,
            Filename=file_path,
            Key=key,
            ExtraArgs={'ACL': 'public-read'},
        )
        print(
            f'Your uploaded file {file_name} can be downloaded from https://{bucket_name}.s3.amazonaws.com/{key}'
        )
    except Exception as e:
        print(e)


def delete_file():
    """
    Method to delete a file from an S3 bucket
    """
    print("Here is a list of your buckets:-")
    list_buckets()
    bucket_name = input(
        '\nEnter the name of the S3 bucket you wish to delete a file from: '
    )
    print("Here is a list of files in the chosen S3 bucket:-")
    list_files(bucket_name)
    key = input(f'\nEnter the key (filename) you wish to delete from {bucket_name}: ')
    try:
        get_client().delete_object(
            Bucket=bucket_name,
            Key=key,
        )
        print(f'The file {key} has been deleted from S3 bucket {bucket_name}')
    except Exception as e:
        print(e)


def download_file():
    """
    Method to download a file from an S3 bucket
    """
    print("Here is a list of your buckets:-")
    list_buckets()
    bucket_name = input(
        '\nEnter the name of the S3 bucket you wish to download a file from: '
    )
    list_files(bucket_name)
    key = input(f'Enter the key (filename) you wish to download from {bucket_name}: ')
    file_path = (
        input(f'Enter the path you wish to download {key} to (default {key}): ') or key
    )
    try:
        get_client().download_file(Bucket=bucket_name, Key=key, Filename=file_path)
        print(f'Downloaded file {key} from S3 bucket {bucket_name} to {file_path}')
    except Exception as e:
        print(e)


if __name__ == '__main__':

    while True:
        # Prompt the user for an input
        prompt = """######## MENU ########
1: List buckets
2: Create a new bucket
3: Delete an existing bucket
4: List files in a bucket
5: Upload a file to a bucket
6: Delete a file from a bucket
7: Download a file from a bucket
Anything else to exit
Choice: """

        try:
            choice = int(input(prompt))
            print()
            if choice == 1:
                list_buckets()
            elif choice == 2:
                create_bucket()
            elif choice == 3:
                delete_bucket()
            elif choice == 4:
                list_files()
            elif choice == 5:
                upload_file()
            elif choice == 6:
                delete_file()
            elif choice == 7:
                download_file()
            else:
                break
            print()
        except ValueError:
            break
        
        
        
# (base) C:\Users\Divyang\Desktop\Final Year B.Tech\T11\Cloud Computing\Assignment 4>python s3.py
# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 1

# Found 3 buckets!
# +-----------------------+---------------------------+
# |          Name         |        CreationDate       |
# +-----------------------+---------------------------+
# |        cc-lab-3       | 2021-12-08 12:09:25+00:00 |
# |      cc-lab4-dark     | 2022-01-13 11:15:39+00:00 |
# | cloud-computing-lab-3 | 2021-12-22 11:14:58+00:00 |
# +-----------------------+---------------------------+

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 2

# Enter a name for your S3 bucket : cc-lab-4
# S3 bucket with name cc-lab-4 has been succesfully created!

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 3

# Here is a list of your buckets:-
# Found 4 buckets!
# +-----------------------+---------------------------+
# |          Name         |        CreationDate       |
# +-----------------------+---------------------------+
# |        cc-lab-3       | 2021-12-08 12:09:25+00:00 |
# |        cc-lab-4       | 2022-01-13 12:34:48+00:00 |
# |      cc-lab4-dark     | 2022-01-13 11:15:39+00:00 |
# | cloud-computing-lab-3 | 2021-12-22 11:14:58+00:00 |
# +-----------------------+---------------------------+

# Enter the name of the S3 bucket you wish to delete: cc-lab4-dark
# S3 bucket with the name cc-lab4-dark has been deleted!

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 1

# Found 3 buckets!
# +-----------------------+---------------------------+
# |          Name         |        CreationDate       |
# +-----------------------+---------------------------+
# |        cc-lab-3       | 2021-12-08 12:09:25+00:00 |
# |        cc-lab-4       | 2022-01-13 12:34:48+00:00 |
# | cloud-computing-lab-3 | 2021-12-22 11:14:58+00:00 |
# +-----------------------+---------------------------+

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 5

# Here is a list of your buckets:-
# Found 3 buckets!
# +-----------------------+---------------------------+
# |          Name         |        CreationDate       |
# +-----------------------+---------------------------+
# |        cc-lab-3       | 2021-12-08 12:09:25+00:00 |
# |        cc-lab-4       | 2022-01-13 12:34:48+00:00 |
# | cloud-computing-lab-3 | 2021-12-22 11:14:58+00:00 |
# +-----------------------+---------------------------+

# Enter the name of the S3 bucket you to upload a file to: cc-lab-4
# Enter the path to the file you wish to upload to cc-lab-4: C:\Users\Divyang\Downloads\commands.txt
# Enter the key (filename) you wish to upload C:\Users\Divyang\Downloads\commands.txt as (default commands.txt): 
# Your uploaded file commands.txt can be downloaded from https://cc-lab-4.s3.amazonaws.com/commands.txt

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 4

# Here is a list of your buckets:-
# Found 3 buckets!
# +-----------------------+---------------------------+
# |          Name         |        CreationDate       |
# +-----------------------+---------------------------+
# |        cc-lab-3       | 2021-12-08 12:09:25+00:00 |
# |        cc-lab-4       | 2022-01-13 12:34:48+00:00 |
# | cloud-computing-lab-3 | 2021-12-22 11:14:58+00:00 |
# +-----------------------+---------------------------+

# Enter the name of the S3 bucket you want a list files for: cc-lab-4
# +--------------+---------------------------+------------------------------------+------+--------------+
# |     Key      |        LastModified       |                ETag                | Size | StorageClass |
# +--------------+---------------------------+------------------------------------+------+--------------+
# | commands.txt | 2022-01-13 12:36:31+00:00 | "5a563ad1d07fabaa377abda003a0381b" | 473  |   STANDARD   |
# +--------------+---------------------------+------------------------------------+------+--------------+

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 7

# Here is a list of your buckets:-
# Found 3 buckets!
# +-----------------------+---------------------------+
# |          Name         |        CreationDate       |
# +-----------------------+---------------------------+
# |        cc-lab-3       | 2021-12-08 12:09:25+00:00 |
# |        cc-lab-4       | 2022-01-13 12:34:48+00:00 |
# | cloud-computing-lab-3 | 2021-12-22 11:14:58+00:00 |
# +-----------------------+---------------------------+

# Enter the name of the S3 bucket you wish to download a file from: cc-lab-4
# +--------------+---------------------------+------------------------------------+------+--------------+
# |     Key      |        LastModified       |                ETag                | Size | StorageClass |
# +--------------+---------------------------+------------------------------------+------+--------------+
# | commands.txt | 2022-01-13 12:36:31+00:00 | "5a563ad1d07fabaa377abda003a0381b" | 473  |   STANDARD   |
# +--------------+---------------------------+------------------------------------+------+--------------+
# Enter the key (filename) you wish to download from cc-lab-4: commands.txt
# Enter the path you wish to download commands.txt to (default commands.txt): 
# Downloaded file commands.txt from S3 bucket cc-lab-4 to commands.txt

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 6

# Here is a list of your buckets:-
# Found 3 buckets!
# +-----------------------+---------------------------+
# |          Name         |        CreationDate       |
# +-----------------------+---------------------------+
# |        cc-lab-3       | 2021-12-08 12:09:25+00:00 |
# |        cc-lab-4       | 2022-01-13 12:34:48+00:00 |
# | cloud-computing-lab-3 | 2021-12-22 11:14:58+00:00 |
# +-----------------------+---------------------------+

# Enter the name of the S3 bucket you wish to delete a file from: cc-lab-4
# Here is a list of files in the chosen S3 bucket:-
# +--------------+---------------------------+------------------------------------+------+--------------+
# |     Key      |        LastModified       |                ETag                | Size | StorageClass |
# +--------------+---------------------------+------------------------------------+------+--------------+
# | commands.txt | 2022-01-13 12:36:31+00:00 | "5a563ad1d07fabaa377abda003a0381b" | 473  |   STANDARD   |
# +--------------+---------------------------+------------------------------------+------+--------------+

# Enter the key (filename) you wish to delete from cc-lab-4: commands.txt
# The file commands.txt has been deleted from S3 bucket cc-lab-4

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# |        cc-lab-4       | 2022-01-13 12:34:48+00:00 |
# | cloud-computing-lab-3 | 2021-12-22 11:14:58+00:00 |
# +-----------------------+---------------------------+

# Enter the name of the S3 bucket you want a list files for: cc-lab-4
# No files found in this bucket! Upload one.

# ######## MENU ########
# 1: List buckets
# 2: Create a new bucket
# 3: Delete an existing bucket
# 4: List files in a bucket
# 5: Upload a file to a bucket
# 6: Delete a file from a bucket
# 7: Download a file from a bucket
# Anything else to exit
# Choice: 9