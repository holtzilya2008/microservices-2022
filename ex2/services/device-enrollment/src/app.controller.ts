import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { AppService } from './app.service';
import { DeviceDto } from './dtos/DeviceDto';
import { EnrollDeviceDto } from './dtos/EnrollDeviceDto';

@Controller('devices')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getAllDevices(): DeviceDto[] {
    return this.appService.getAllDevices();
  }

  @Get(':id')
  getDeviceById(@Param('id') id: string): DeviceDto {
    return this.appService.getDeviceById(id);
  }

  @Post()
  enrollDevice(@Body() deviceDto: EnrollDeviceDto): DeviceDto {
    return this.appService.enrollDevice(deviceDto);
  }
}
