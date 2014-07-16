#!/bin/csh

echo "Running LIVV test suite on titan."
echo
echo "To run tests without rebuilding, use skip-build."
echo

@ skip_build_set = ($1 == skip-build)

#pushd . > /dev/null

if ($skip_build_set == 0) then
 cd ../../../builds/titan-gnu
 csh titan-gnu-build-and-test-serial.csh skip-tests 
 csh titan-gnu-build-and-test.csh skip-tests 
 cd ../titan-pgi
 csh titan-pgi-build-and-test.csh skip-tests 
 exit
endif

cd ../../../tests/higher-order/livv
csh run_livv_default_tests.csh 

#popd . > /dev/null
