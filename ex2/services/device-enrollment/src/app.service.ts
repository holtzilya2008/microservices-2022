import { Injectable } from '@nestjs/common';
import { DeviceDto } from './dtos/DeviceDto';
import { EnrollDeviceDto } from './dtos/EnrollDeviceDto';
import { v4 } from 'uuid';

@Injectable()
export class AppService {
  private devices: DeviceDto[] = [];

  getAllDevices(): DeviceDto[] {
    return this.devices;
  }

  getDeviceById(id: string): any {
    return this.devices.find((device) => device.id === id);
  }

  enrollDevice(deviceProps: EnrollDeviceDto): DeviceDto {
    const device = {
      ...deviceProps,
      id: v4(),
      enrolledAt: new Date(),
    };

    this.devices.push(device);
    return device;
  }
}
