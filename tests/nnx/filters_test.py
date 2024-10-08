# Copyright 2024 The Flax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from absl.testing import absltest

from flax import nnx


class TestFilters(absltest.TestCase):
  def test_path_contains(self):
    class Model(nnx.Module):
      def __init__(self, rngs):
        self.backbone = nnx.Linear(2, 3, rngs=rngs)
        self.head = nnx.Linear(3, 10, rngs=rngs)

    model = Model(nnx.Rngs(0))

    head_state = nnx.state(model, nnx.PathContains('head'))

    self.assertIn('head', head_state)
    self.assertNotIn('backbone', head_state)

if __name__ == '__main__':
  absltest.main()
