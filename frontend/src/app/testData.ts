export const testData = {
  containers: [
    {
      id: '2915ef21981d',
      name: 'nervous_elbakyan',
      image: 'ubuntu',
      status: 'Exited',
      creation_date: '2020.03.10 11:59',
      command: '/bin/bash',
      ports: []
    },
    {
      id: '3b366f08ae6d',
      name: 'exciting_roentgen',
      image: 'ubuntu',
      status: 'Created',
      creation_date: '2020.02.09 10:29',
      command: '/bin/bash',
      ports: []
    },
    {
      id: '0c5678281814',
      name: 'flamboyant_chatterjee',
      image: 'ubuntu',
      status: 'Up',
      creation_date: '2020.03.12 10:00',
      command: '/entrypoint.sh',
      ports: ['8080']
    },
    {
      id: '41c5b4c5cd6a',
      name: 'jolly_montalcini',
      image: 'centos',
      status: 'stopped',
      creation_date: '2020.03.11 09:19',
      command: 'run.sh',
      ports: ['22']
    },
    {
      id: '72d24b7da7532e',
      name: 'jolly_roentgen',
      image: 'nodejs',
      status: 'Up',
      creation_date: '2020.03.12 08:00',
      command: 'node',
      ports: ['80', '8080']
    },
    {
      id: '35f3ad2b7c0ca',
      name: 'exciting_elbakyan',
      image: 'scala-sbt',
      status: 'Exited',
      creation_date: '2020.01.20 02:50',
      command: 'sbt assembly',
      ports: []
    }
  ],
  images: [
    {
      id: '2915ef21981d',
      repository: 'ubuntu',
      tag: 'latest',
      size: '64.2 MB',
      creation_date: '2020.02.09 10:29'
    },
    {
      id: 'dc246327c2a9',
      repository: 'centos',
      tag: 'latest',
      size: '30.1 MB',
      creation_date: '2020.03.11 09:19'
    },
    {
      id: '52cae6b7620',
      repository: 'scala-sbt',
      tag: 'latest',
      size: '128.5 MB',
      creation_date: '2020.01.20 02:50'
    },
    {
      id: 'd2401ca631d',
      repository: 'nodejs',
      tag: '13',
      size: '10 MB',
      creation_date: '2020.03.12 08:00'
    }
  ]
};
