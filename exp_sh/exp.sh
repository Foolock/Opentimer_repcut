exp_object=("original_taskflow_tbb_ftask_only" "partition_taskflow_tbb_2_queues_schedule_ftaskonly")

for obj in ${exp_object[@]}
do
  cd ./$obj/
  bash exp.sh
  cd ../
done
