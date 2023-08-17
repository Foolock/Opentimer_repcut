num=(2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20)
exp_object=("c17" "des_perf" "tv80" "wb_dma" "vga_lcd" "ac97_ctrl" "aes_core")

for obj in ${exp_object[@]}
  do
    cd ./benchmark/$obj/
    rm *.txt
    cd ../../
  done

for n in ${num[@]} 
do
  sed -i "s/tbb::global_control::max_allowed_parallelism, std::thread::hardware_concurrency()/tbb::global_control::max_allowed_parallelism, $n/g" "./ot/timer/timer.cpp"
  sed -i "s/mt_kahypar_partition_id_t _set_num_partition = 20;/mt_kahypar_partition_id_t _set_num_partition = $n;/g" "./ot/timer/timer.hpp"
  cd ./build
  make -j 8
  cd ../
  for obj in ${exp_object[@]} 
  do
    cd ./benchmark/$obj/
    rm tbb_2_queue_pftask_only_log_t${n}_p${n}.txt
    python3 ../../exp.py "*******************thread = $n, partition = $n, circuit: $obj*******************" >> tbb_2_queue_pftask_only_log_t${n}_p${n}.txt
    for i in 1 2 3 4 5 6 7 8 9 10
    do
      ../../bin/ot-shell < $obj.conf >> tbb_2_queue_pftask_only_log_t${n}_p${n}.txt
    done
    cd ../../
  done
  sed -i "s/tbb::global_control::max_allowed_parallelism, $n/tbb::global_control::max_allowed_parallelism, std::thread::hardware_concurrency()/g" "./ot/timer/timer.cpp"
  sed -i "s/mt_kahypar_partition_id_t _set_num_partition = $n;/mt_kahypar_partition_id_t _set_num_partition = 20;/g" "./ot/timer/timer.hpp"
done

