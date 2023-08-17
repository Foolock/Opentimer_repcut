exp_object=("original_taskflow_tbb_ftask_only" "partition_taskflow_tbb_2_queues_schedule_ftaskonly")

benchmarks=("c17" "des_perf" "tv80" "wb_dma" "vga_lcd" "ac97_ctrl" "aes_core")

for obj in ${exp_object[@]}
do
  cd ./$obj/
  for benchmark in ${benchmarks[@]} 
  do
    cd ./benchmark/$benchmark/
    rm *.txt
    cd ../../
  done
  cd ../
done

