# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/macc',
                'doc_host': 'https://niyazikemer.github.io',
                'git_url': 'https://github.com/niyazikemer/macc',
                'lib_path': 'macc'},
  'syms': { 'macc.datasets': { 'macc.datasets.DataLoaders': ('datasets.html#dataloaders', 'macc/datasets.py'),
                               'macc.datasets.DataLoaders.__init__': ('datasets.html#dataloaders.__init__', 'macc/datasets.py'),
                               'macc.datasets.DataLoaders.from_dd': ('datasets.html#dataloaders.from_dd', 'macc/datasets.py'),
                               'macc.datasets.collate_dict': ('datasets.html#collate_dict', 'macc/datasets.py'),
                               'macc.datasets.get_dls': ('datasets.html#get_dls', 'macc/datasets.py'),
                               'macc.datasets.inplace': ('datasets.html#inplace', 'macc/datasets.py')},
            'macc.learn': { 'macc.learn.Callback': ('learner.html#callback', 'macc/learn.py'),
                            'macc.learn.CancelBatchException': ('learner.html#cancelbatchexception', 'macc/learn.py'),
                            'macc.learn.CancelEpochException': ('learner.html#cancelepochexception', 'macc/learn.py'),
                            'macc.learn.CancelFitException': ('learner.html#cancelfitexception', 'macc/learn.py'),
                            'macc.learn.DeviceCB': ('learner.html#devicecb', 'macc/learn.py'),
                            'macc.learn.DeviceCB.__init__': ('learner.html#devicecb.__init__', 'macc/learn.py'),
                            'macc.learn.DeviceCB.before_batch': ('learner.html#devicecb.before_batch', 'macc/learn.py'),
                            'macc.learn.DeviceCB.before_fit': ('learner.html#devicecb.before_fit', 'macc/learn.py'),
                            'macc.learn.LRFinderCB': ('learner.html#lrfindercb', 'macc/learn.py'),
                            'macc.learn.LRFinderCB.__init__': ('learner.html#lrfindercb.__init__', 'macc/learn.py'),
                            'macc.learn.LRFinderCB.after_batch': ('learner.html#lrfindercb.after_batch', 'macc/learn.py'),
                            'macc.learn.LRFinderCB.before_fit': ('learner.html#lrfindercb.before_fit', 'macc/learn.py'),
                            'macc.learn.LRFinderCB.cleanup_fit': ('learner.html#lrfindercb.cleanup_fit', 'macc/learn.py'),
                            'macc.learn.Learner': ('learner.html#learner', 'macc/learn.py'),
                            'macc.learn.Learner.__getattr__': ('learner.html#learner.__getattr__', 'macc/learn.py'),
                            'macc.learn.Learner.__init__': ('learner.html#learner.__init__', 'macc/learn.py'),
                            'macc.learn.Learner._fit': ('learner.html#learner._fit', 'macc/learn.py'),
                            'macc.learn.Learner._one_batch': ('learner.html#learner._one_batch', 'macc/learn.py'),
                            'macc.learn.Learner._one_epoch': ('learner.html#learner._one_epoch', 'macc/learn.py'),
                            'macc.learn.Learner.callback': ('learner.html#learner.callback', 'macc/learn.py'),
                            'macc.learn.Learner.fit': ('learner.html#learner.fit', 'macc/learn.py'),
                            'macc.learn.Learner.one_epoch': ('learner.html#learner.one_epoch', 'macc/learn.py'),
                            'macc.learn.Learner.training': ('learner.html#learner.training', 'macc/learn.py'),
                            'macc.learn.MetricsCB': ('learner.html#metricscb', 'macc/learn.py'),
                            'macc.learn.MetricsCB.__init__': ('learner.html#metricscb.__init__', 'macc/learn.py'),
                            'macc.learn.MetricsCB._log': ('learner.html#metricscb._log', 'macc/learn.py'),
                            'macc.learn.MetricsCB.after_batch': ('learner.html#metricscb.after_batch', 'macc/learn.py'),
                            'macc.learn.MetricsCB.after_epoch': ('learner.html#metricscb.after_epoch', 'macc/learn.py'),
                            'macc.learn.MetricsCB.before_epoch': ('learner.html#metricscb.before_epoch', 'macc/learn.py'),
                            'macc.learn.MetricsCB.before_fit': ('learner.html#metricscb.before_fit', 'macc/learn.py'),
                            'macc.learn.MomentumLearner': ('learner.html#momentumlearner', 'macc/learn.py'),
                            'macc.learn.MomentumLearner.__init__': ('learner.html#momentumlearner.__init__', 'macc/learn.py'),
                            'macc.learn.MomentumLearner.zero_grad': ('learner.html#momentumlearner.zero_grad', 'macc/learn.py'),
                            'macc.learn.SingleBatchCB': ('learner.html#singlebatchcb', 'macc/learn.py'),
                            'macc.learn.SingleBatchCB.after_batch': ('learner.html#singlebatchcb.after_batch', 'macc/learn.py'),
                            'macc.learn.TrainCB': ('learner.html#traincb', 'macc/learn.py'),
                            'macc.learn.TrainCB.__init__': ('learner.html#traincb.__init__', 'macc/learn.py'),
                            'macc.learn.TrainCB.backward': ('learner.html#traincb.backward', 'macc/learn.py'),
                            'macc.learn.TrainCB.get_loss': ('learner.html#traincb.get_loss', 'macc/learn.py'),
                            'macc.learn.TrainCB.predict': ('learner.html#traincb.predict', 'macc/learn.py'),
                            'macc.learn.TrainCB.step': ('learner.html#traincb.step', 'macc/learn.py'),
                            'macc.learn.TrainCB.zero_grad': ('learner.html#traincb.zero_grad', 'macc/learn.py'),
                            'macc.learn.TrainLearner': ('learner.html#trainlearner', 'macc/learn.py'),
                            'macc.learn.TrainLearner.backward': ('learner.html#trainlearner.backward', 'macc/learn.py'),
                            'macc.learn.TrainLearner.get_loss': ('learner.html#trainlearner.get_loss', 'macc/learn.py'),
                            'macc.learn.TrainLearner.predict': ('learner.html#trainlearner.predict', 'macc/learn.py'),
                            'macc.learn.TrainLearner.step': ('learner.html#trainlearner.step', 'macc/learn.py'),
                            'macc.learn.TrainLearner.zero_grad': ('learner.html#trainlearner.zero_grad', 'macc/learn.py'),
                            'macc.learn.collate_device': ('learner.html#collate_device', 'macc/learn.py'),
                            'macc.learn.lr_find': ('learner.html#lr_find', 'macc/learn.py'),
                            'macc.learn.run_cbs': ('learner.html#run_cbs', 'macc/learn.py'),
                            'macc.learn.to_cpu': ('learner.html#to_cpu', 'macc/learn.py'),
                            'macc.learn.to_device': ('learner.html#to_device', 'macc/learn.py'),
                            'macc.learn.with_cbs': ('learner.html#with_cbs', 'macc/learn.py'),
                            'macc.learn.with_cbs.__call__': ('learner.html#with_cbs.__call__', 'macc/learn.py'),
                            'macc.learn.with_cbs.__init__': ('learner.html#with_cbs.__init__', 'macc/learn.py')}}}
