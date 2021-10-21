#!/bin/bash

while true
do
  count=$(ps -ef | grep -c kk_test)
  if [ $count -lt 2 ] 
    the
     # 改动项 查询第1块gpu的容量--2p 第2块3p--2  第三块--4p  第四块--5p
     stat2=$(gpustat | awk '{print $14}' | sed -n '3p')
     memory=`echo  ${stat2} | tr -cd "[0-9]" `
     minmemory=1000
     if [ ${memory} -lt ${minmemory} ]
       then
         echo 'run'
         #改动项 前面输入占用的gpu id 后面是运行代码
         python model_train.py --data_path ../final_dataset --gnn_model jknet --hidden_dim 64 --n_layers 4 --fanout 10,10,10,10 --batch_size 1024 --GPU 1 --out_path outputs
     fi
  fi
  sleep 2
done
