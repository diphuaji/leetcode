<?php
    function twoSum($nums, $target) {
        $numsMap = [];
        $result = [];
        for($i=0; $i<count($nums); $i++){
            $num = $nums[$i];
            if(!key_exists($num,$numsMap)){
                $numsMap[$num] = [$i];
                continue;
            }
            $numsMap[$num][] = $i;
        }
        
        for($i=0; $i<count($nums); $i++){
            $result[] = $i;
            if($value=$numsMap[$target-$nums[$i]]??null){
                if(count($value)>1){
                    $result = $value;
                }else{
                    $result[] = $value[0];
                }
                break;
            }
            array_pop($result);
        }
        
        return $result;
    }
    var_dump(twoSum([2,3,7,9],9));
