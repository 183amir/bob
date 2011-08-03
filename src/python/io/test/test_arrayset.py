#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Wed 03 Aug 2011 12:33:08 CEST 

"""Some tests to arraysets
"""

import os, sys
import unittest
import torch

class ArraysetTest(unittest.TestCase):
  """Performs various tests for the Torch::io::Arrayset objects"""

  def test01_extend1d(self):

    # shows how to use the extend() method on arraysets.

    t = torch.io.Arrayset()
    data = torch.core.array.float32_2(range(50), (25,2))
    t.extend(data, 0)

    self.assertEqual( len(t), 25 )
    self.assertEqual( t.elementType, torch.io.ElementType.float32 )
    self.assertEqual( t.shape, (2,) )

    for i, k in enumerate(t):
      self.assertTrue ( data[i,:].numeq(k.get()) )

    # we can achieve the same effect with lists
    t = torch.io.Arrayset()
    vdata = [data[k,:] for k in range(data.extent(0))]
    t.extend(vdata)

    self.assertEqual( len(t), 25 )
    self.assertEqual( t.elementType, torch.io.ElementType.float32 )
    self.assertEqual( t.shape, (2,) )

    for i, k in enumerate(t):
      self.assertTrue ( vdata[i].numeq(k.get()) )

  def test02_extend2d(self):

    # shows how to use the extend() method on arraysets.

    t = torch.io.Arrayset()
    data = torch.core.array.float64_3(range(90), (3,10,3))
    t.extend(data, 1)

    self.assertEqual( len(t), 10 )
    self.assertEqual( t.elementType, torch.io.ElementType.float64 )
    self.assertEqual( t.shape, (3,3) )

    for i, k in enumerate(t):
      self.assertTrue ( data[:,i,:].numeq(k.get()) )

    # we can achieve the same effect with lists once more
    t = torch.io.Arrayset()
    vdata = [data[:,k,:] for k in range(data.extent(1))]
    t.extend(vdata)

    self.assertEqual( len(t), 10 )
    self.assertEqual( t.elementType, torch.io.ElementType.float64 )
    self.assertEqual( t.shape, (3,3) )

    for i, k in enumerate(t):
      self.assertTrue ( vdata[i].numeq(k.get()) )

  def test03_extend3d(self):

    # shows how to use the extend() method on arraysets.

    t = torch.io.Arrayset()
    data = torch.core.array.complex128_4(range(540), (3,4,15,3))
    t.extend(data, 2)

    self.assertEqual( len(t), 15 )
    self.assertEqual( t.elementType, torch.io.ElementType.complex128 )
    self.assertEqual( t.shape, (3,4,3) )

    for i, k in enumerate(t):
      self.assertTrue ( data[:,:,i,:].numeq(k.get()) )

    # we can achieve the same effect with lists once more
    t = torch.io.Arrayset()
    vdata = [data[:,:,k,:] for k in range(data.extent(2))]
    t.extend(vdata)

    self.assertEqual( len(t), 15 )
    self.assertEqual( t.elementType, torch.io.ElementType.complex128 )
    self.assertEqual( t.shape, (3,4,3) )

    for i, k in enumerate(t):
      self.assertTrue ( vdata[i].numeq(k.get()) )

if __name__ == '__main__':
  sys.argv.append('-v')
  if os.environ.has_key('TORCH_PROFILE') and \
      os.environ['TORCH_PROFILE'] and \
      hasattr(torch.core, 'ProfilerStart'):
    torch.core.ProfilerStart(os.environ['TORCH_PROFILE'])
  os.chdir(os.path.realpath(os.path.dirname(sys.argv[0])))
  os.chdir('data')
  unittest.main()
  if os.environ.has_key('TORCH_PROFILE') and \
      os.environ['TORCH_PROFILE'] and \
      hasattr(torch.core, 'ProfilerStop'):
    torch.core.ProfilerStop()
